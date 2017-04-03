import socket
import struct


server_address = ('localhost', 90)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(server_address)

while True:
    try:
        print "which operation do you wanna do?"
        print "+ - * / %"
        string = raw_input()
        print "how many numbers do you wanna " + string
        counter = int(raw_input())

        for i in range(0, counter):
            number = int(raw_input())
            number = struct.pack('i', number)
            string += number

        s.send(string)
        print 'result:', s.recv(1024), "\n"
    except Exception:
        print "something happened, sorry :(\n"
        continue

s.close()
