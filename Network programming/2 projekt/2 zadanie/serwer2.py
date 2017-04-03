import socket
import datetime

daytime=datetime.datetime

print("Wybierz typ serwera:")
typ=input()
print("Wybierz protokol serwera: (daytime/time")
protokol=input()

if typ.lower() == "daytime":
    port=13
    adres_serwera=('localhost', port)

    if protokol.upper()=='TCP':
        protokol= socket.SOCK_STREAM
        s=socket.socket(socket.AF_INET, protokol)
        print("Ok serwer TCP dziala")
        s.bind(adres_serwera)
        s.listen(5)

        while True:
            polaczenie, adres_klienta= s.accept()
            data=str(daytime.utcnow())

            polaczenie.send(data)
            print("Wyslano date klientowi o adresie: ", adres_klienta," Podano date: ",data)
            polaczenie.close()

    elif protokol.upper()=='UDP':
        prtokol=socket.SOCK_DGRAM
        print("Ok serwer UDP dziala")
        s=socket.socket(socket.AF_INET, protokol)
        s.bind(adres_serwera)

        while True:
            try:
                wiadomosc, adres_klienta=address.recvfrom(1024)
                wiadomosc=str(daytime.utcnow())

                print("Wyslano date klientowi o adresie: ",adres_klienta,"Wyslana data to:", wiadomosc)
                s.sendto(wiadomosc,adres_klienta)

            except KayboardInterrupt:
                s.close()

    else :
        raise Exception ("Wybrano zly protokol serwera, wybierz UDP lub TCP")







elif typ.lower()=="time":
    port=37
    adres_serwera=('localhost',port)

    if protokol.upper()=="TCP":
        protokol = socket.SOCK_STREAM

        s = socket.socket(socket.AF_INET, protokol)
        print("OK serwer TCP dziala")
        s.bind(adres_serwera)
        s.listen(5)

        while True:
            connection, adres_klienta = s.accept()
            time = int((daytime.utcnow() - datetime.datetime(1900, 1, 1)).total_seconds())

            message = bytearray([0, 0, 0, 0])
            message[0] = (time >>24) & 0xff
            message[1] = (time >>16) & 0xff
            message[2] = (time >>8) & 0xff
            message[3] = (time) & 0xff

            connection.send(message)
            print (adres_klienta, " ", message)

            connection.close()

    elif protokol.upper() == "UDP":
        protokol = socket.SOCK_DGRAM

        s = socket.socket(socket.AF_INET, protokol)
        s.bind(adres_serwera)
        print("Ok serwer UDP dziala")
        while True:
            try:
                message, address = s.recvfrom(1024)
                time = int((daytime.utcnow() - datetime.datetime(1900, 1, 1)).total_seconds())

                message = bytearray([0, 0, 0, 0])
                message[0] = (time >>24) & 0xff
                message[1] = (time >>16) & 0xff
                message[2] = (time >>8) & 0xff
                message[3] = (time) & 0xff

                s.sendto(message, address)

                print( address, " ", message)
            except KeyboardInterrupt:
                s.close()
    else:
         raise Exception("Podano zly protokol serwera, wybierz TCP lub UDP")
else:
    raise Exception("Podano zly typ serwera, wybierz TCP lub UDP")





