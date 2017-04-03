def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

do_ktorej=(input('Wpisz (int) do ktorej liczby chcesz wydrukowac ciag Fibonacciego: '))

for liczba in range(1,do_ktorej+1,1):
    print liczba,":  ", fibonacci(liczba)