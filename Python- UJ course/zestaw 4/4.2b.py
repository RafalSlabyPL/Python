def rysowanie():
    while True:
        try:
            x = int(raw_input("Podaj wartosc x(int): "))
            y = int(raw_input("Podaj wartosc y(int): "))
        except ValueError:
            print "Nie wpisani liczby calkowitej"
            continue
        else:
            if x > 0 and y > 0 and x < 10 and y < 10:
                break
            else:
                print "Wartosci x i y musza byc wieksze od 0 i mniejsze od 10"
                continue

    prosta1 = "+"
    for a in range(1, x+1, 1):
        prosta1 += "---"
        prosta1 += "+"
    for a in range(1, y+1, 1):
        print prosta1
        print prosta1.replace("+", "|").replace("-", " ")
    return prosta1

print rysowanie()