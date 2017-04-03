def wpisywanie():
    while True:
        try:
            min = int(raw_input("Podaj wartosc (int) min miarki: "))
            max = int(raw_input("Podaj wartosc (int) maz miarki: "))
        except ValueError:
            print "Nie wpisani liczby dajacej sie zaokraglic do liczbyt calkowitej"
            continue
        else:
            if min<max:
                break
            else:
                print "Wartosc minimalna miarki nie moze byc wieksza lub rowna maksymalnej. Wpisz ponownie"
                continue
    return [min,max]

def rysowanie():
    kropki="....."
    spacje="   "
    linijka1="  |"
    linijka2=(str(dlugosc[0]).zfill(3)).replace("0"," ")
    kreska="|"
    for x in range(int(dlugosc[0]),dlugosc[1],1):
        linijka1 += kropki
        linijka1 += kreska

    for x in range(int(dlugosc[0]),dlugosc[1],1):
        linijka2 += spacje
        linijka2 += str(dlugosc[0]+1).zfill(3)
        dlugosc[0] +=1
    print linijka1
    print linijka2.replace("0"," ")
    pass

dlugosc=wpisywanie()
rysowanie()