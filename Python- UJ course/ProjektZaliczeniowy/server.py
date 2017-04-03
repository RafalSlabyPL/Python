#!/usr/bin/python

import socket
from thread import *
from random import SystemRandom
from math import pow
from time import sleep
import threading
import ciphers
import sys
import os

TCP_IP = 'localhost'
TCP_PORT = 50005
BUFFER_SIZE = 1024
PRIME = 20
BASE = 12
keys = {}


def check_config():
    global TCP_IP, TCP_PORT, BUFFER_SIZE, PRIME, BASE
    pathConfig = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_server.rc")
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


def check_option():
    for argument in sys.argv:
        if argument == "-h" or argument == "--help":
            pathHelp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "help.txt")
            File = open(pathHelp, "r")
            print File.read()
            sys.exit()


def calculate_key(conn):
    cryptography = SystemRandom()
    randomNumber = cryptography.randint(1, 30)
    clientNumber = conn.recv(BUFFER_SIZE)
    myNumber = pow(BASE, randomNumber) % PRIME
    conn.send(str(myNumber))
    key = pow(float(clientNumber), randomNumber) % PRIME
    return key


def new_client(conn):
    haveKey = False
    global keys
    while True:
        if haveKey == False:
            try:
                keys[threading.currentThread().ident] = calculate_key(conn)
                haveKey = True
            except socket.error:
                sleep(1)
                continue
            break
    while True:
        try:
            data = conn.recv(BUFFER_SIZE)
            data = data.split(":")
            try:
                print data[0] + ":" + ciphers.caesar_cipher(data[1], -int(keys[threading.currentThread().ident]))
            except IndexError:
                print "Odlaczono klienta"
                sys.exit()
        except socket.error:
            print "Odlaczono klienta"
            sys.exit()
    conn.close(data)


# main
check_config()
check_option()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
        print 'Connected by', addr
        start_new_thread(new_client, (conn,))
    except (KeyboardInterrupt, SystemExit):
        print "Zamknales server. Dobranoc"
        sys.exit()
s.close()
