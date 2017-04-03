import math as m

def heron(a, b, c):
    if a + b <= c or a+c <= b or c + b <= a:
        raise ValueError
    elif not isinstance(a, (float,int)) or not isinstance(b, (float,int)) or not isinstance(c, (float,int)):
        raise TypeError
    else:
        s = (a + b + c) / 2.0
        return m.sqrt(s * (s - a) * (s - b) * (s-c))

print heron(1, 3, 3.5)