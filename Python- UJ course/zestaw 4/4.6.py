lista = [2, 8, -4, 11, (1, 4, 7), [8, 8], [5, 5]]  # oczekiwana suma to 55


def sumowanie(lista):
    x = 0
    suma_liczb = 0
    for suma in lista:
        if isinstance(suma, (list, tuple)):
            for liczba in suma:
                x += liczba
        else:
            x = suma
        suma_liczb += x
        x = 0
    print suma_liczb
    pass


sumowanie(lista)
