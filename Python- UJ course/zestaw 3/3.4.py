while True:
    x=raw_input("Podaj liczbe lub nappisz stop: ")
    if x.lower()=="stop":
        print "Wpisano STOP. Przerywam dzialanie programu"
        break
    try:
        number1=float(x)
        print "Podana liczba to: ", number1
        print "Jej 2 potega to: ", number1**2
        print "3 potega tej liczby to: ", number1**3
        continue
    except ValueError:
        print "Podanie nierozpoznany napis. Prosze wpisac liczbe calkowita lub \"stop\" w celu zakonczenia programu"
        continue