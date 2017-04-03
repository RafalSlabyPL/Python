import socket
print("Wpisz port: ")
port = int(input())
print("Wpisz powitanie na serwerze: ")
wprowadzone = input()

powitanie=wprowadzone.encode()
print("Ile razy chesz powtorzyc otrzymana wiadomosc klientowi?")
ile = int(input())
print("OK, to serwer dziala!")

s_adres = ("localhost", port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(s_adres)
s.listen(5)

while True:
    connection, c_adres = s.accept()
    message = connection.recv(512)
    paaaaaaanie_cooooo_to_bylo = message.decode()
    if message:
        connection.sendall(powitanie)
    else:
        continue

    for i in range(0 , ile):
        connection.sendall(message)

    print ("Adres klienta:",c_adres,", powtarzana wiadomosc:", paaaaaaanie_cooooo_to_bylo,", Port:", port)
    print("Polaczenie zakonczone")
    connection.close()
