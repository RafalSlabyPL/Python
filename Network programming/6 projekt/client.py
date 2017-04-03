import socket
import base64
import hashlib
from crypto import Random
from crypto.Cipher import AES
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


addres = 'localhost'#raw_input()
port = 90#int(raw_input())
key = sys.argv[1]#raw_input()

server_address = (addres, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

aes = AESCipher(key)
message = aes.encrypt('something ')

s.send(message)
received_data = ''

while True:
    data = s.recv(24)

    if data:
        received_data += data
    else:
        print received_data
        data = aes.decrypt(received_data)
        print data
        break
s.close()
