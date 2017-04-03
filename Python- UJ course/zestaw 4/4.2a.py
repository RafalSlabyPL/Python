def rysowanie():
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

    kropki="....."
    spacje="   "
    linijka1="  |"
    linijka2=(str(min).zfill(3)).replace("0"," ")
    kreska="|"
    for x in range(int(min),max,1):
        linijka1 += kropki
        linijka1 += kreska

    for x in range(int(min),max,1):
        linijka2 += spacje
        linijka2 += str(min+1).zfill(3)
        min +=1
    #print linijka1
    #print linijka2.replace("0"," ")
    return [linijka1,linijka2.replace("0"," ")]

linijka=rysowanie()
print linijka[0]
print linijka[1]