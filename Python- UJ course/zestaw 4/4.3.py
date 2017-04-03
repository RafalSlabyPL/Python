def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(input('Podaj x w celu wykonania dzialania"!x": '))