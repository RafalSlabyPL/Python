import random as r
import math as m

def calc_pi(n=100):
    """Obliczanie liczby pi metoda Monte Carlo.
    n oznacza liczbe losowanych punktow."""

    in_circle = 0

    for i in range(0, n):
        x2 = r.random()**2
        y2 = r.random()**2
        if m.sqrt(x2 + y2) < 1.0:
            in_circle += 1
    return (in_circle / float(n)) * 4

print calc_pi(10000000)