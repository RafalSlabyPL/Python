#!/usr/bin/python

from random import SystemRandom
from math import pow

def getMessage():
    print "Podaj wiadomosc:"
    return raw_input()

def getKey():
    print "Podaj klucz:"
    key = int(input())
    if (key >= 1 and key <= 26):
        return key

def getMode():
    while True:
        print "Wpisz o, zeby odszyfrowac, albo z, zeby zaszyfrowac:"
        mode = raw_input()
        if(mode == "o" or mode == "z"):
            return mode
def getKeyWord():
    print "Podaj slowo kluczowe:"
    return raw_input()

def caesar_cipher(message, key):
    result = ""
    key = int(key)
    for letter in message:
        if letter.isalpha():
            number = ord(letter) + key
            if letter.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            elif letter.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
            result += chr(number)
        else:
            result += letter
    return result

def vigener_cipher(message, keyWord):
    row = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    VigenerTab = [0 for i in range(0, 26)]
    indexOfKeyWord = 0
    for index in range(len(row)):
        VigenerTab[index] = row[index:] + row[:index]
    for letter in range(len(message)):
        if message[letter].isalpha():
            columnNumber = VigenerTab[0].index(message[letter])
            RowNumber = 0
            for iterator in range(26):
                if VigenerTab[0][iterator] == keyWord[indexOfKeyWord % len(keyWord)]:
                    RowNumber = iterator
                    break
            translated += VigenerTab[RowNumber][columnNumber]
            indexOfKeyWord += 1
        else:
            translated += message[letter]
    return translated

def one_time_pad_encrypt(message):
    key = ""
    cipher = ""
    cryptography = SystemRandom()
    for i in xrange(len(message) + 100):
        key += chr(cryptography.randrange(65, 90))
    for x in range(len(message)):
        if message[x].isalpha():
            number = ord(message[x]) + ord(key[x]) - 130
            if number >= 26:
                number -= 26
            cipher += chr(number + 65)
        else:
            cipher += message[x]
    return (cipher, key)

def one_time_pad_decrypt(key, cipher):
    translated = ""
    for x in range(len(cipher)):
        if cipher[x].isalpha():
            number = ord(cipher[x]) - ord(key[x])
            if number < 0:
                number += 26
            translated += chr(number + 65)
        else:
            translated += cipher[x]
    return translated

def Diffie_Hellman_key_exchange(p,q):
    print "Liczba pierwsza: %d" %p
    print "baza: %d" %q
    cryptography = SystemRandom()
    a = cryptography.randint(1,10)
    print "Alicja wybrala liczbe: %d" %a
    A = pow(q, a) % p
    print "Alicja wyslala do Boba liczbe: %d" %A
    b = cryptography.randint(1,10)
    print "Bob wybral liczbe: %d" %b
    B = pow(q, b) % p
    print "Bob wyslal do Alicji liczbe: %d" %B

    k = pow(B,a) % p
    h = pow(A,b) % p
    print "Alicja: %d" %k
    print "Bob: %d" %h

'''
#szyfr cezara
message = getMessage()
key = getKey()
if getMode() == "o":
    key = - key
print caesar_cipher(message, key)

#Szyfr Vigenera
keyWord = getKeyWord().upper()
message = getMessage().upper()
print vigener_cipher(message, keyWord)

#one time pad
message = getMessage().upper()
if getMode() == "o":
    key = getKeyWord()
    print one_time_pad_decrypt(key, message)
else:
    cipher, key = one_time_pad_encrypt(message)
    print cipher
    print key

#protokol Diffiego-Hellmana
DiffieHellman_key_exchange(12,27)
'''
