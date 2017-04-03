def znajdz_pusta(plansza, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if plansza[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if plansza[x][y] == 0:
                return x, y
    return -1, -1


def sprawdzenie(plansza, i, j, pole):
    rzad = all([pole != plansza[i][x] for x in range(9)])
    if rzad:
        columna = all([pole != plansza[x][j] for x in range(9)])
        if columna:
            TopX, TopY = 3 * (i / 3), 3 * (j / 3)
            for x in range(TopX, TopX + 3):
                for y in range(TopY, TopY + 3):
                    if plansza[x][y] == pole:
                        return False
            return True
    return False


def rozwiaz_Sudoku(plansza, i=0, j=0):
    i, j = znajdz_pusta(plansza, i, j)
    if i == -1:
        return True
    for pole in range(1, 10):
        if sprawdzenie(plansza, i, j, pole):
            plansza[i][j] = pole
            if rozwiaz_Sudoku(plansza, i, j):
                return True
            plansza[i][j] = 0
    return False





dane = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
rozwiaz_Sudoku(dane)
print dane
#[[5, 1, 7, 6, 9, 8, 2, 3, 4], [2, 8, 9, 1, 3, 4, 7, 5, 6], [3, 4, 6, 2, 7, 5, 8, 9, 1], [6, 7, 2, 8, 4, 9, 3, 1, 5], [1, 3, 8, 5, 2, 6, 9, 4, 7], [9, 5, 4, 7, 1, 3, 6, 8, 2], [4, 9, 5, 3, 6, 2, 1, 7, 8], [7, 2, 3, 4, 8, 1, 5, 6, 9], [8, 6, 1, 9, 5, 7, 4, 2, 3]]
