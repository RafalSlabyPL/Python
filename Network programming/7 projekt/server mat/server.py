import socket
import threading
import struct


class SocketProvider:
    def __init__(self, address, port):
        self.server_address = (address, int(port))
        self.server_address2 = (address, int(port)+1)

    def connection(self):
        raise NotImplementedError

    def connection2(self):
        raise NotImplementedError

    def close_connection(self):
        raise NotImplementedError

    def receive_message(self):
        raise NotImplementedError

    def send_message(self, message):
        raise NotImplementedError


class TCPProvider(SocketProvider):
    connect = None
    connect2 = None
    s = None
    s2 = None

    def connection(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(self.server_address)
            self.s.listen(2)

        except Exception:
            return "ups, something happened"

    def connection2(self):
        try:
            self.s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s2.bind(self.server_address2)
            self.s2.listen(2)
            self.connect2, client_address = self.s2.accept()

        except Exception:
            return "ups, something happened"

    def wait_for_client(self):
        self.connect, client_address = self.s.accept()

    def close_connection(self):
        self.connect.close()
        self.connect2.close()

    def close_socket(self):
        self.s.close()
        self.s2.close()

    def receive_message(self):
        return self.connect.recv(1024)

    def send_message(self, message):
        self.connect.send(message)


class UDPProvider(SocketProvider):
    s = None
    s2 = None
    address = None
    address2 = None

    def connection(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.bind(self.server_address)

        except Exception:
            return "ups, something happened"

    def connection2(self):
        try:
            self.s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s2.bind(self.server_address2)
            message, self.address2 = self.s2.recvfrom(1024)

        except Exception:
            return "ups, something happened"

    def wait_for_client(self):
        return self.receive_message()

    def close_connection(self):
        pass

    def close_socket(self):
        self.s.close()
        self.s2.close()

    def receive_message(self):
        message, self.address = self.s.recvfrom(1024)
        return message

    def send_message(self, message):
        self.s.sendto(message, self.address)


class Server(threading.Thread):
    def __init__(self, type):
        threading.Thread.__init__(self)
        self.type = type.lower()

    def run(self):
        if self.type == 'udp':
            self.provider = UDPProvider("localhost", 90)
            self.provider.connection()

            while True:
                message = self.provider.wait_for_client()
                t = Connection(self.provider, message)
                t.start()

        elif self.type == "tcp":
            self.provider = TCPProvider('localhost', 90)
            self.provider.connection()

            while True:
                self.provider.wait_for_client()
                t = Connection(self.provider)
                t.start()
        else:
            raise Exception("bad type")


class Connection(threading.Thread):
    def __init__(self, provider, message=None):
        threading.Thread.__init__(self)
        self.provider = provider
        self.message = message

    def run(self):
        while True:
            try:
                if self.message:
                    message = self.message
                    #print message
                    self.message = None
                else:
                    message = self.provider.receive_message()
                    #print message

                if message[0] == "+":
                    result = 0
                    i = 1
                    while i <= len(message) - 4:
                        mess = struct.unpack('i', message[i:i+4])
                        result += mess[0]
                        i += 4

                    self.provider.send_message(str(result))

                elif message[0] == "-":
                    result = 0
                    i = 1

                    while i <= len(message) - 4:
                        if i == 1:
                            mess = struct.unpack('i', message[i:i+4])
                            result = mess[0]
                            i += 4
                            continue

                        mess = struct.unpack('i', message[i:i+4])
                        result -= mess[0]
                        i += 4

                    self.provider.send_message(str(result))
                elif message[0] == "*":
                    result = 1
                    i = 1

                    while i <= len(message) - 4:
                        mess = struct.unpack('i', message[i:i+4])
                        result *= mess[0]
                        i += 4

                    self.provider.send_message(str(result))
                elif message[0] == "/":
                    i = 1

                    while i <= len(message) - 4:
                        if i == 1:
                            mess = struct.unpack('i', message[i:i+4])
                            result = float(mess[0])
                            i += 4
                            continue

                        mess = struct.unpack('i', message[i:i+4])
                        result /= float(mess[0])
                        i += 4

                    self.provider.send_message(str(result))

                elif message[0] == "%":
                    i = 1

                    while i <= len(message) - 4:
                        if i == 1:
                            mess = struct.unpack('i', message[i:i+4])
                            result = mess[0]
                            i += 4
                            continue

                        mess = struct.unpack('i', message[i:i+4])
                        result %= mess[0]
                        i += 4

                    self.provider.send_message(str(result))
            except Exception as e:
                self.provider.send_message("error: " + str(e))

tcp = Server('tcp')
udp = Server('udp')
tcp.start()
udp.start()
