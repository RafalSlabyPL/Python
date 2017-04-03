def WprowadzanieMacierzy():
    Macierz = []
    PobieranieWiersza = lambda x: list(map(float, input(x).split()))
    Wiersz = PobieranieWiersza("Wprowadz wiersz macierzy: ")
    Macierz.append(Wiersz)
    WymiarMacierzy = len(Wiersz)
    for i in range(WymiarMacierzy - 1):
        KolejnyWiersz = PobieranieWiersza("Wprowadz wiersz macierzy: ")
        if len(KolejnyWiersz) == WymiarMacierzy:
            Macierz.append(KolejnyWiersz)
        else:
            raise Exception('Maciez stopnia ' + str(WymiarMacierzy)+" musi miec " + str(WymiarMacierzy) + "liczb w wierszu")
    return Macierz


def IloczynSkalarny(m, x, y):
    suma = 0
    if x == 0 or y == 0:
        return suma
    else:
        for idx in range(min(x, y)):
            suma += m[x][idx] * m[idx][y]
        return suma


def Rozklad_LU(Macierz):
    rozmiar = len(Macierz)
    index = 0
    while index <= rozmiar:
        for j in range(index, rozmiar):
            Macierz[index][j] -= IloczynSkalarny(Macierz, index, j)
        for i in range(index + 1, rozmiar):
            Macierz[i][index] = (Macierz[i][index] - IloczynSkalarny(Macierz, i, index)) / Macierz[index][index]
        index += 1
    L = [[] for i in range(rozmiar)]
    U = [[] for i in range(rozmiar)]
    for i in range(rozmiar):
        for j in range(rozmiar):
            if i == j:
                L[i].append(1)
                U[i].append(Macierz[i][j])
            elif i > j:
                L[i].append(Macierz[i][j])
                U[i].append(0)
            else:
                L[i].append(0)
                U[i].append(Macierz[i][j])
    return L, U


def DrukowanieMacierzyLU(L, U):
    print("Macierz L:")
    print(L)
    print("Macierz U:")
    print(U)

# main program

L, U = Rozklad_LU(WprowadzanieMacierzy())
DrukowanieMacierzyLU(L, U)

