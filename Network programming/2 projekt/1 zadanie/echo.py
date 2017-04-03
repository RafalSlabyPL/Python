import socket

port = 7


while True:
    print ("Wpisz z jakiego protokolu chcesz korzystac(TCP/UDP): ")
    protokol = (input())

    if protokol.upper() == "TCP":
        protocol = socket.SOCK_STREAM
        print ("ok no to TCP")
        break
    elif protokol.upper() == "UDP":
        protocol = socket.SOCK_DGRAM
        print ("ok no to UDP")
        break
    else:
        print("Nie wybrano protokolu. Wybierz TCP lub UDP")


s_address = ('localhost', port)
s = socket.socket(socket.AF_INET, protocol)
print("OK, serwer dziala")
s.bind(s_address)

if protocol==socket.SOCK_STREAM:
    s.listen()
    while True:
        connection, client_address = s.accept()
        while True:
            message = connection.recv(24)
            print ("Cos jest!")

            if message:
                print ("Wysylam...")
                connection.send(message)
            else:
                print ("Brak danych do odeslania")
                break
            print ("Ok, koniec petli")

        print ("Adres klienta: ", client_address, ", Otrzymana wiadomosc: ", message.decrypt())
        connection.close()
        print("Program zakonczyl dzialanie")


elif protocol == socket.SOCK_DGRAM:
    while True:
        message, client_address=s.recvfrom(1024)
        if message:
            print("Ok, cos jest!")
            print(message)
            s.sendto(message,client_address)
        else:
            print ("Brak danych do odeslania")
            break
        print("Adres klienta: ", client_address, ", Otrzymana wiadomosc: ", message)
    s.close()
else:
    raise Exception ("Nastapil nieznany blad")