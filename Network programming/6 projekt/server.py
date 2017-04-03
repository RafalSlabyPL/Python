import socket
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import sys

class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


port = 90#int(raw_input())
mess = sys.argv[1]#raw_input()
x = int(sys.argv[2])#int(raw_input())
key = sys.argv[3]#raw_input()

server_address = ('localhost', port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(server_address)
s.listen(1)

aes = AESCipher(key)

try:
    while True:
        connection, client_address = s.accept()
        message = connection.recv(1024)

        message = aes.decrypt(message)
        print client_address, " ", message

        #mess = aes.encrypt(mess)
        #connection.send(mess)
        message_to_send = mess + "\n"

        for i in range(0, x):
            message_to_send += message + "\n"

        #print message_to_send
        message = aes.encrypt(str(message_to_send))
        #print message
        connection.send(message)

        connection.close()
except KeyboardInterrupt:
    s.close()
