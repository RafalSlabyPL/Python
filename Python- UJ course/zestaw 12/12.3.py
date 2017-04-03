from math import floor

def pancake_sort(lista):
    max_poz = lambda lst: lista.index(max(lst))

    for rozmiar in reversed(range(len(lista))):
        maximum = max_poz(lista[:rozmiar + 1])
        odwracanie(lista, 0, maximum)
        odwracanie(lista, 0, rozmiar)
    return lista

def odwracanie(lista, start, koniec):
    while start < koniec:
        lista[start], lista[koniec] = lista[koniec], lista[start]
        start += 1
        koniec -= 1


def mediana_sort(lista):
    lista = pancake_sort(lista)
    if len(lista) % 2 == 0:
        return (lista[(len(lista) / 2) - 1] + lista [len(lista)/2]) / 2.0
    else:
        return lista[len(lista) / 2 ]

a = [4, 7, 1, 3, 2, 6, 5]
print a
print mediana_sort(a)
