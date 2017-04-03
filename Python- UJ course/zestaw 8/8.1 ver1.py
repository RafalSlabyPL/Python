def solve1(a, b, c):
    """Rozwiazywanie rownania liniowego a x + b y + c = 0."""
    #(a / b)x + c / b = y
    for x in range(-10, 11, 1):
        print [x, (a / b) * x + c / b]
    pass

solve1(2, 1, 1)