from random import randint

def wyszukiwanie_linowe(lista, wyszukiwany_element):
    pozycja = 0
    wyniki =[]
    for x in lista:
        if x == wyszukiwany_element:
            wyniki.append(pozycja)
        pozycja += 1
    return wyniki

def tworzenie_listy(n):
    lista = []
    for element in range(0, n, 1):
        x = randint(0, n-1)
        lista.append(x)
    return lista

print wyszukiwanie_linowe(tworzenie_listy(100), 5)