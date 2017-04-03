
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
