#!/usr/bin/python

import socket
from random import SystemRandom
from time import sleep
from math import pow
import ciphers
import sys
import os

TCP_IP = 'localhost'
TCP_PORT = 50005
BUFFER_SIZE = 1024
PRIME = 20
BASE = 12
TRY_NUMBER = 3


def check_config():
    global TCP_IP, TCP_PORT, BUFFER_SIZE, PRIME, BASE, TRY_NUMBER
    pathConfig = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_client.rc")
    with open(pathConfig) as f:
        for line in f:
            if "TCP_IP" in line:
                TCP_IP = line[9::].rstrip('\n')
            elif "TCP_PORT" in line:
                TCP_PORT = int(line[11::])
            elif "BUFFER_SIZE" in line:
                BUFFER_SIZE = int(line[14::])
            elif "PRIME" in line:
                PRIME = int(line[8::])
            elif "BASE" in line:
                BASE = int(line[7::])
            elif "TRY_NUMBER" in line:
                TRY_NUMBER = int(line[13::])

def check_option():
    for argument in sys.argv:
        if argument == "-h" or argument == "--help":
            pathHelp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "help.txt")
            File = open(pathHelp, "r")
            print File.read()
            sys.exit()


def send(s, username):
    while True:
        message = raw_input()
        try:
            s.send(username + ": " + ciphers.caesar_cipher(message, key))
        except socket.error:
            print "Nastapil juz koniec pracy serwera"
        if message == "bye":
            print "Klient zakonczyl juz prace. Mozesz go bezpiecznie wylaczyc"
            sys.exit()


def calculate_key(s):
    cryptography = SystemRandom()
    randomNumber = cryptography.randint(1, 30)
    myNumber = pow(BASE, randomNumber) % PRIME
    s.send(str(myNumber))
    serverNumber = float(s.recv(BUFFER_SIZE))
    key = pow(serverNumber, randomNumber) % PRIME
    return key


def check_server():
    num = 0
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
        except socket.error:
            num += 1
            if num == TRY_NUMBER:
                print "Koncze prace, nie znalazlem serwera :("
                sys.exit()
            else:
                print "Nie znalazlem serwera, za chwile sprobuje jeszcze raz! :)"
                sleep(5)
            continue
        return s


# main
check_config()
check_option()
s = check_server()

username = raw_input("Podaj swoja nazwe uzytkownika: ")
key = calculate_key(s)

while True:
    try:
        send(s, username)
    except KeyboardInterrupt:
        print "Zamknales recznie klienta"
        sys.exit()
