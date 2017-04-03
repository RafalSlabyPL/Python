import socket
print("Wpisz port: ")
port = int(input())
print("Wprowadz wiadomosc ktora zostanie wprowadzona na serwer: ")
wprowadzenie = input()
wiadomosc = wprowadzenie.encode()
print("Ok, to dzialamy:")



s_adres = ("localhost", port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(s_adres)
s.sendall(wiadomosc)

while True:
    plik = s.recv(512)
    wypisanie=plik.decode()
    
    if plik:
        print (wypisanie)
    else:
        break
s.close()
