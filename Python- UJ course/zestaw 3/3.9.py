lista = [[], [4], (1, 2), [3, 4],(5, 6, 7)]


def sumowanie(lista):
    x = 0
    robocza_lista = []
    for suma in lista:
        if isinstance(suma, (list,tuple)):
            for liczba in suma:
                x += liczba
        else:
            x = suma
        robocza_lista.append(x)
        x = 0


    print robocza_lista


sumowanie(lista)
