import asyncore
import socket
import sqlite3
import threading

class Server():
    s = asyncore.dispatcher()
    s_to_message = asyncore.dispatcher()
    server_address = None
    server_address2 = None
    conn = None
    c = None

    def __init__(self):
        asyncore.dispatcher.__init__(self.s)
        asyncore.dispatcher.__init__(self.s_to_message)
        self.s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.set_reuse_addr()
        self.s_to_message.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_to_message.set_reuse_addr()
        self.server_address = ('localhost', 11000)
        self.server_address2 = ('localhost', 11001)

        self.conn = sqlite3.connect('MyDatabase.db')
        self.c = self.conn.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS users (name VARCHAR(50) PRIMARY KEY, password VARCHAR(50))''')
        #self.c.execute('''INSERT INTO users VALUES ('Gulish', 'haha9ha')''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS friends (name VARCHAR(50), friend_name VARCHAR(50), unique(name, friend_name))''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS user_information (name VARCHAR(50), status VARCHAR(15), description VARCHAR(50))''')
        self.conn.commit()


    def set_connection(self):
        self.s.bind(self.server_address)
        self.s.listen(10)

        self.s_to_message.bind(self.server_address2)
        self.s_to_message.listen(10)

    def wait_for_client(self):
        return self.s.accept()

    def wait_for_client_message(self):
        return self.s_to_message.accept()


"""
class ClientConnected(threading.Thread):
    def __init__(self):
        threading.Thread.__init__()


    def run(self):
"""

serv = Server()
serv.set_connection()
connections = []

send_message = []

while True:
    pair = serv.wait_for_client()

    if pair:
        connection, client_address = pair
        m_connetion, m_address = serv.wait_for_client_message()
        #connection with client, name of client, message status, name of person who send message, message
        connection = [connection, "", 0, "", "", m_connetion]
        connections.append(connection)
    else:
        if connections:
            pass
        else:
            continue


    for connection in connections:
        if connection[2] == 1:
            index = connections.index(connection)
            connections[index][2] = 0

            connection[5].send(connection[4] + "\n")

            connections[index][3] = ""
            connections[index][4] = ""

        try:
            data = connection[0].recv(1024)
        except socket.error:
            continue

        if data:
            exist = False

            if data[0:3] == 'log':

                data = data[4:]

                index = data.index(" ")

                for string in serv.c.execute("SELECT * FROM users WHERE name='%s' and password='%s'" % (data[0:index], data[index+1:])):
                    exist = True

                if exist == True:
                    user_name = data[0:index]

                    index = connections.index(connection)
                    connections[index][1] = user_name

                    serv.c.execute("UPDATE user_information SET status='Online' WHERE name='%s'" % connection[1])
                    serv.conn.commit()

                    connection[0].send("Login successful")
                else:
                    connection[0].send("This user not exist")

            if data[0:8] == 'register':
                data = data[9:]

                index = data.index(" ")

                for string in serv.c.execute("SELECT * FROM users WHERE name='%s'" % data[0:index]):
                    exist = True

                if exist == True:
                    connection[0].send("This login is unavailable")
                else:
                    connection[0].send("Registration successful")
                    serv.c.execute("INSERT INTO users VALUES ('%s', '%s')" % (data[0:index], data[index+1:]))
                    serv.c.execute("INSERT INTO user_information VALUES ('%s', 'Offline', 'Description...')" % data[0:index])
                    serv.conn.commit()

            if data[0:6] == "search":
                index = data.index(" ")

                for string in serv.c.execute("SELECT * FROM users WHERE name='%s'" % data[index+1:]):
                    exist = True

                if exist == True:
                    connection[0].send("Search successful")
                else:
                    connection[0].send("Search failed")

            if data[0:3] == "add":
                index = data.index(" ")

                try:
                    serv.c.execute("INSERT INTO friends VALUES ('%s', '%s')" % (connection[1], data[index+1:]))
                    serv.c.execute("INSERT INTO friends VALUES ('%s', '%s')" % (data[index+1:], connection[1]))
                    serv.conn.commit()

                    connection[0].send("Successful")
                except sqlite3.IntegrityError:
                    connection[0].send("You are already friends with him")

            if data[0:4] == "show":
                exist = False
                friends = []
                j = 0

                for string in serv.c.execute("SELECT * FROM friends WHERE name='%s'" % connection[1]):
                    friends.append(string[1])
                    exist = True

                for j in range(0, len(friends)):
                    for i in serv.c.execute("SELECT status, description FROM user_information WHERE name='%s'" % friends[j]):
                        connection[0].send("(" + i[0] + ")" + " " + friends[j] + " " + "-" + " " + i[1] + " ' ")

                if not exist:
                    connection[0].send("There are no friends of you")

                connection[0].send("<EOF>")

            if data[0:4] == "send":
                data = data.split(" ")

                index = -99

                for i in connections:
                    if i[1] == data[1]:
                        index = connections.index(i)
                    else:
                        continue

                if index == -99:
                    continue

                connections[index][2] = 1
                connections[index][3] = data[2]
                connections[index][4] = " ".join(data[3:])

            if data[0:6] == "status":
                data = data.split(" ")

                serv.c.execute("UPDATE user_information SET status='%s' WHERE name='%s'" % (data[1], connection[1]))
                serv.conn.commit()

            if data[0:3] == "set":
                data = data.split(" ")
                data = " ".join(data[1:])

                serv.c.execute("UPDATE user_information SET description='%s' WHERE name='%s'" % (data, connection[1]))
                serv.conn.commit()


