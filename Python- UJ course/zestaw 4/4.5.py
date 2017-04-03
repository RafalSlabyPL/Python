lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def odwracanie (lista, start, end):
    start -= 1
    lista=lista[0:start] + lista[start:end][::-1] + lista[end::]
    return lista

print odwracanie(lista, 2, 7)