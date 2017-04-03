from math import fabs

import random as r
r.seed()

#Returns the square of the random value (random value of the interval <-1,1>
def KwadratLosowej():
    return ((r.random() - 0.5)*2)**2

#Sums n consecutive squares of random variable
def SumaNElementow(n):
    NowaSuma = 0
    for x in range(1, n+1):
        NowaSuma += KwadratLosowej()
    return NowaSuma

#Calculates the % which occupies n redundant sphere, with r = 1 in n dimensioned hypercube with edge x = 2
def obliczanie(n):
    WewnatrzKuli = 0
    PozaKula = 0
    for number in range (0, 10000000):
        SumaKwadratow = SumaNElementow(n)
        if SumaKwadratow <= 1:
            WewnatrzKuli += 1
        else:
            PozaKula += 1
            continue
    return (float(WewnatrzKuli)/10000000)

def silnia(n):
      if n>1:
            return n*silnia(n-1)
      else:
            return 1

def analitycznie(wymiar, r):
    pi = 3.14159265359
    if wymiar%2 == 0:
        m = wymiar / 2
        return ((pi**m)/silnia(m)) * r**(2*m)
    else:
        m = (wymiar-1)/2
        return ((2**((2*m)+1) * silnia(m) * pi**m) / silnia((2*m)+1)) * (r**(2*m+1))



# main()
for wymiar in range(1,30):
    temp1 = obliczanie(wymiar) * (2 ** wymiar)
    temp2 = analitycznie(wymiar,1)
    print("Numerycznie: Kula ", wymiar,"D: ", temp1, "J^", wymiar)
    print("Analitycznie: Kula ", wymiar,"D: ", temp2, "J^", wymiar)
    print("Blad bezwzględny: ", fabs(temp2-temp1))
    print("Blad względny: ", (fabs(temp2-temp1)/temp2)*100,"%")
    print()