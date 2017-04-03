from random import gauss
import random as r
r.seed()

def calkowicie_losowe(n):
    lista = []
    for element in range(0, n, 1):
        x = r.randint(0, 100)
        lista.append(x)
    return lista

def prawie_posortowsne(n):
    lista = []
    for element in range(0, n, 1):
        x = r.randint(element - 3, element + 3)
        lista.append(x)
    return lista

def odwrocone_prawie_posortowane(n):
    lista = []
    for element in range(0, n, 1):
        x = r.randint(element - 3, element + 3)
        lista.append(x)
    return odwracanie(lista, 0, n-1)

def odwracanie(lista, start, koniec):
    while start < koniec:
        lista[start], lista[koniec] = lista[koniec], lista[start]
        start += 1
        koniec -= 1
    return lista

def losowe_o_rozkladzie_gausowskim(n, srodek, wariancja):
    values = []
    while len(values) < n:
        value = gauss(srodek, wariancja)
        if srodek - 50 < value < srodek + 50:
            values.append(value)
    return values

def n_liczb_o_wartosciach_powtarzajacych_sie(n): # n elementowy zbior, k elementow gdzie k < n i k > 0
    lista = []
    for element in range(0, n, 1):
        x = r.randint(0, n-1)
        lista.append(x)
    return odwracanie(lista, 0, n-1)

