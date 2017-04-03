import socket
import sys


host = address=(str)(sys.argv[1])
protokol=(str)(sys.argv[2])
min=(int)(sys.argv[3])
max=(int)(sys.argv[4]+1)


if protokol.upper()== 'TCP':

    def skanuj_port (numer_portu, host):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(5)
      try:
          s = s.connect((host, numer_portu))
          print "Port: ",numer_portu, "[+] Port otwarty"

      except Exception, e:
          print "Port: ",numer_portu, "[-] Port zamkniety"




    for i in range(min, max):
        skanuj_port(i, host)






elif protokol.upper()== 'UDP':

    def skanuj_port_UDP (numer_portu, host):
        server_address = (host, numer_portu)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(5)
        s.sendto("Echoooooo?", server_address)
        try:
            s.recvfrom(4096)
            print "Port: ",numer_portu, "[+] Port otwarty"
        except Exception, e:
          print "Port: ",numer_portu, "[-] Port zamkniety"

    for i in range(min, max):
        skanuj_port_UDP (i, host)