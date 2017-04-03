import socket
import sys
import random
import threading
from enum import Enum
import os


class State(Enum):
    void = 10
    ship = 20
    sunk = 30
    down = 40

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

    def receive_answer(self):
        raise NotImplementedError

    def send_message(self, message):
        raise NotImplementedError


class ClientProvider(SocketProvider):
    s = None
    s2 = None

    def connection(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(self.server_address)
        except Exception:
            return "ups, something happened"

    def connection2(self):
        try:
            self.s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s2.connect(self.server_address2)

        except Exception:
            return "ups, something happened"

    def close_connection(self):
        self.s.close()
        self.s2.close()

    def receive_message(self):
        return self.s.recv(1024)

    def receive_answer(self):
        return self.s2.recv(1024)

    def send_message(self, message):
        self.s.send(message)

    def send_coordinate(self, message):
        self.s2.send(message)

class ServerProvider(SocketProvider):
    connect = None
    connect2 = None
    s = None
    s2 = None

    def connection(self):
        global turn
        turn = True

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(self.server_address)
            self.s.listen(1)
            self.connect, client_address = self.s.accept()

        except Exception:
            return "ups, something happened"

    def connection2(self):
        try:
            self.s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s2.bind(self.server_address2)
            self.s2.listen(1)
            self.connect2, client_address = self.s2.accept()

        except Exception:
            return "ups, something happened"

    def close_connection(self):
        self.connect.close()
        self.connect2.close()

    def close_socket(self):
        self.s.close()
        self.s2.close()

    def receive_message(self):
        return self.connect.recv(1024)

    def receive_answer(self):
        return self.connect2.recv(1024)

    def send_message(self, message):
        self.connect.send(message)

    def send_coordinate(self, message):
        self.connect2.send(message)


class BattleShip:
    provider = None
    board = []
    enemy_board = []

    turn = None
    counter = 0
    message = ''

    def __init__(self, address, type, port):
        self.address = address
        self.type = type.lower()
        self.port = port

        self.board = [[State.void for x in range(10)] for y in range(10)]
        self.enemy_board = [[State.void for x in range(10)] for y in range(10)]

        if self.type == "client":
            self.turn = False
            self.provider = ClientProvider(address, port)
        elif self.type == "server":
            self.turn = True
            self.provider = ServerProvider(address, port)

    def connection(self):
        self.provider.connection()
        self.provider.connection2()

    def check_direction(self, random_position, j):
        if random_position + j > 9:
            return -1
        elif random_position - j < 0:
            return 1
        else:
            vertical_direction = random.randint(-100, 100)

            if vertical_direction >= 0:
                return 1
            else:
                return -1

    def check_position(self, board, horizontal_position, vertical_position):
        if board[horizontal_position][vertical_position] == State.ship:
            return False

        if horizontal_position == 0 and vertical_position == 0:
            if board[horizontal_position][vertical_position+1] != State.ship \
                    and board[horizontal_position+1][vertical_position] != State.ship \
                    and board[horizontal_position+1][vertical_position+1] != State.ship:
                return True
            else:
                return False

        elif horizontal_position == 9 and vertical_position == 9:
            if board[horizontal_position][vertical_position-1] != State.ship \
                    and board[horizontal_position-1][vertical_position] != State.ship \
                    and board[horizontal_position-1][vertical_position-1] != State.ship:
                return True
            else:
                return False

        elif horizontal_position == 0 and vertical_position == 9:
            if board[horizontal_position+1][vertical_position] != State.ship \
                    and board[horizontal_position][vertical_position-1] != State.ship \
                    and board[horizontal_position+1][vertical_position-1] != State.ship:
                return True
            else:
                return False

        elif horizontal_position == 9 and vertical_position == 0:
            if board[horizontal_position][vertical_position+1] != State.ship \
                    and board[horizontal_position-1][vertical_position] != State.ship \
                    and board[horizontal_position-1][vertical_position-1] != State.ship:
                return True
            else:
                return False

        elif horizontal_position == 0:
            if board[horizontal_position+1][vertical_position+1] != State.ship \
                    and board[horizontal_position+1][vertical_position] != State.ship \
                    and board[horizontal_position+1][vertical_position-1] != State.ship \
                    and board[horizontal_position][vertical_position+1] != State.ship \
                    and board[horizontal_position][vertical_position-1] != State.ship:
                return True
            else:
                return False

        elif vertical_position == 0:
            if board[horizontal_position][vertical_position+1] != State.ship \
                    and board[horizontal_position+1][vertical_position+1] != State.ship \
                    and board[horizontal_position+1][vertical_position] != State.ship \
                    and board[horizontal_position-1][vertical_position+1] != State.ship \
                    and board[horizontal_position-1][vertical_position] != State.ship:
                return True
            else:
                return False

        elif horizontal_position == 9:
            if board[horizontal_position-1][vertical_position+1] != State.ship \
                    and board[horizontal_position-1][vertical_position] != State.ship \
                    and board[horizontal_position-1][vertical_position-1] != State.ship \
                    and board[horizontal_position][vertical_position+1] != State.ship \
                    and board[horizontal_position][vertical_position-1] != State.ship:
                return True
            else:
                return False

        elif vertical_position == 9:
            if board[horizontal_position][vertical_position-1] != State.ship \
                    and board[horizontal_position+1][vertical_position-1] != State.ship \
                    and board[horizontal_position+1][vertical_position] != State.ship \
                    and board[horizontal_position-1][vertical_position-1] != State.ship \
                    and board[horizontal_position-1][vertical_position] != State.ship:
                return True
            else:
                return False

        else:
            if board[horizontal_position][vertical_position+1] != State.ship \
                    and board[horizontal_position][vertical_position-1] != State.ship \
                    and board[horizontal_position+1][vertical_position] != State.ship \
                    and board[horizontal_position-1][vertical_position] != State.ship \
                    and board[horizontal_position+1][vertical_position+1] != State.ship \
                    and board[horizontal_position-1][vertical_position-1] != State.ship \
                    and board[horizontal_position+1][vertical_position-1] != State.ship \
                    and board[horizontal_position-1][vertical_position+1] != State.ship:
                return True
            else:
                return False

    def fill_board(self):
        ships_number = 1
        cells_number = 4
        counter_cells = 0
        counter_ships = 0

        buffor = [[State.void for x in range(10)] for y in range(10)]

        while True:
            random_vertical_position = random.randint(0, 9)
            random_horizontal_position = random.randint(0, 9)


            if not self.check_position(self.board, random_horizontal_position, random_vertical_position):
                continue

            vertical_direction = self.check_direction(random_vertical_position, cells_number)
            horizontal_direction = self.check_direction(random_horizontal_position, cells_number)

            random_direction = random.randint(0, 1)

            if ships_number == 1:
                while True:
                    if self.check_position(self.board, random_horizontal_position, random_vertical_position):
                        buffor[random_horizontal_position][random_vertical_position] = State.ship
                        counter_cells += 1

                        if random_direction == 0:
                            random_horizontal_position += horizontal_direction
                        else:
                            random_vertical_position += vertical_direction
                    else:
                        counter_cells = 0
                        buffor = [[State.void for x in range(10)] for y in range(10)]

                    if counter_cells == cells_number:
                        counter_cells = 0

                        for n in range(0, 10):
                            for m in range(0, 10):
                                if buffor[n][m] == State.ship:
                                    self.board[n][m] = State.ship
                                    buffor[n][m] = State.void
                        break

            elif ships_number == 2:
                while True:
                    if self.check_position(self.board, random_horizontal_position, random_vertical_position):
                        buffor[random_horizontal_position][random_vertical_position] = State.ship
                        counter_cells += 1

                        if random_direction == 0:
                            random_horizontal_position += horizontal_direction
                        else:
                            random_vertical_position += vertical_direction
                    else:
                        counter_cells = 0

                        random_vertical_position = random.randint(0, 9)
                        random_horizontal_position = random.randint(0, 9)

                        vertical_direction = self.check_direction(random_vertical_position, cells_number)
                        horizontal_direction = self.check_direction(random_horizontal_position, cells_number)

                        buffor = [[State.void for x in range(10)] for y in range(10)]

                    if counter_cells == cells_number:
                        counter_ships += 1
                        counter_cells = 0

                        random_vertical_position = random.randint(0, 9)
                        random_horizontal_position = random.randint(0, 9)

                        vertical_direction = self.check_direction(random_vertical_position, cells_number)
                        horizontal_direction = self.check_direction(random_horizontal_position, cells_number)

                        for n in range(0, 10):
                            for m in range(0, 10):
                                if buffor[n][m] == State.ship:
                                    self.board[n][m] = State.ship
                                    buffor[n][m] = State.void

                    if counter_ships == ships_number:
                        counter_ships = 0
                        break

            elif ships_number == 3:
                while True:
                    if self.check_position(self.board, random_horizontal_position, random_vertical_position):
                        buffor[random_horizontal_position][random_vertical_position] = State.ship
                        counter_cells += 1

                        if random_direction == 0:
                            random_horizontal_position += horizontal_direction
                        else:
                            random_vertical_position += vertical_direction
                    else:
                        counter_cells = 0
                        random_vertical_position = random.randint(0, 9)
                        random_horizontal_position = random.randint(0, 9)

                        vertical_direction = self.check_direction(random_vertical_position, cells_number)
                        horizontal_direction = self.check_direction(random_horizontal_position, cells_number)

                        buffor = [[State.void for x in range(10)] for y in range(10)]

                    if counter_cells == cells_number:
                        counter_ships += 1
                        counter_cells = 0

                        random_vertical_position = random.randint(0, 9)
                        random_horizontal_position = random.randint(0, 9)

                        vertical_direction = self.check_direction(random_vertical_position, cells_number)
                        horizontal_direction = self.check_direction(random_horizontal_position, cells_number)

                        for n in range(0, 10):
                            for m in range(0, 10):
                                if buffor[n][m] == State.ship:
                                    self.board[n][m] = State.ship
                                    buffor[n][m] = State.void

                    if counter_ships == ships_number:
                        counter_ships = 0
                        break

            elif ships_number == 4:
                while True:
                    random_vertical_position = random.randint(0, 9)
                    random_horizontal_position = random.randint(0, 9)

                    if self.check_position(self.board, random_horizontal_position, random_vertical_position):
                        buffor[random_horizontal_position][random_vertical_position] = State.ship
                        counter_cells += 1
                    else:
                        counter_cells = 0
                        buffor = [[State.void for x in range(10)] for y in range(10)]

                    if counter_cells == cells_number:
                        counter_ships += 1
                        counter_cells = 0

                        for n in range(0, 10):
                            for m in range(0, 10):
                                if buffor[n][m] == State.ship:
                                    self.board[n][m] = State.ship
                                    buffor[n][m] = State.void

                    if counter_ships == ships_number:
                        counter_ships = 0
                        break
            else:
                break

            ships_number += 1
            cells_number -= 1

    def print_board(self):
        for i in range(11):
            if i > 0:
                sys.stdout.write(str(i-1) + " ")
            else:
                sys.stdout.write(" ")

            for j in range(10):
                if i == 0:
                    sys.stdout.write(" " + str(j))
                    continue

                if self.board[i-1][j] == State.void:
                    sys.stdout.write(("%c " % 219))
                elif self.board[i-1][j] == State.ship:
                    sys.stdout.write("o ")
                elif self.board[i-1][j] == State.sunk:
                    sys.stdout.write("x ")
                elif self.board[i-1][j] == State.down:
                    sys.stdout.write("m ")
                else:
                    pass

            print ""

    def print_enemy_board(self):
        for i in range(11):
            if i > 0:
                sys.stdout.write(str(i-1) + " ")
            else:
                sys.stdout.write(" ")

            for j in range(10):
                if i == 0:
                    sys.stdout.write(" " + str(j))
                    continue

                if self.enemy_board[i-1][j] == State.void:
                    sys.stdout.write(("%c " % 219))
                elif self.enemy_board[i-1][j] == State.down:
                    sys.stdout.write("m ")
                elif self.enemy_board[i-1][j] == State.sunk:
                    sys.stdout.write("x ")
                else:
                    pass

            print ""


class ChatReceiver(threading.Thread):
    def __init__(self, provider):
        threading.Thread.__init__(self)
        self.provider = provider

    def run(self):
        while True:
            try:
                ship.message += self.provider.receive_message() + "\n"

            except Exception:
                continue

class CoordinateReceiver(threading.Thread):
    def __init__(self, ship, provider):
        threading.Thread.__init__(self)
        self.ship = ship
        self.provider = provider

    def run(self):
        while True:
            message = self.provider.receive_answer()

            if message[0] == "r":
                x = int(message[2])
                y = int(message[4])

                if self.ship.board[x][y] == State.ship:
                    self.ship.board[x][y] = State.sunk
                    if self.ship.check_position(self.ship.board, x, y):
                        self.provider.send_coordinate("You sank my battleship!")
                    else:
                        self.provider.send_coordinate("You hit my battleship!")
                else:
                    ship.board[x][y] == State.down
                    ship.turn = True

                    self.provider.send_coordinate("Miss!")

                    print "your round"
            else:
                if message == "Miss!":
                    ship.turn = False
                elif message[:3] == "You":
                    ship.counter += 1

                    if ship.counter == 20:
                        print "you Won!"
                        self.provider.send_coordinate("you Lost!")
                        os._exit(1)

                elif message == "you Lost!":
                    print message
                    os._exit(1)

                print message


ship = BattleShip(address=sys.argv[1], type=sys.argv[2], port=sys.argv[3])

ship.connection()

t = ChatReceiver(ship.provider)
t.start()
t2 = CoordinateReceiver(ship, ship.provider)
t2.start()
ship.fill_board()
ship.print_board()

while True:
    command = raw_input().lower()

    if command == 'help':
        print "command list:\ns <message> - send message\nb <my/enemy> - show my/enemy board\nr <coordinate> - " \
              "round in game\n"
    elif command == "read":
        print ship.message
        ship.message = ''

    elif command[0] == "s":
        if command[1] == " ":
            message = command[2:]
            ship.provider.send_message(message)
        else:
            print "bad command"
    elif command[0] == "b":
        if command[2:] == "my":
            ship.print_board()
        elif command[2:] == "enemy":
            ship.print_enemy_board()
    elif command[0] == "r":
        try:
            if ship.turn:
                if command[1] == " " and int(command[2]) < 10 and command[3] == " " and int(command[4]) < 10 \
                        and int(command[2]) >= 0 and int(command[4]) >= 0:

                    ship.provider.send_coordinate(command)
                else:
                    print "bad command or bad coordinate"
            else:
                print "please, wait for your round"

        except Exception:
            print "bad command or bad coordinate"
    else:
        print "bad command"



