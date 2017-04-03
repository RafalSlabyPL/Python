def NWD (a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a



class frac(object):
    def __init__ (self, licznik, mianownik):
        if mianownik ==0:
            raise ValueError("Mianownik nie moze byc 0")

        else:
            self.ulamek = [licznik / NWD(licznik, mianownik), mianownik / NWD(licznik, mianownik)]

        pass


    def __str__(self):
        if self.ulamek[0] == 0:
            return "0"

        elif self.ulamek[0] % self.ulamek[1] == 0:
            return str(self.ulamek[0]/self.ulamek[1])

        else:
            return str(self.ulamek)


    def __add__(self, other):
        a = self.ulamek[0] * other.ulamek[1] + other.ulamek[0] * self.ulamek[1]
        b = other.ulamek[1] * self.ulamek[1]
        return frac(a / (NWD (a, b)), b / NWD(a, b))


    def __sub__ (self,other):
        a = self.ulamek[0] * other.ulamek[1] - other.ulamek[0] * self.ulamek[1]
        b = other.ulamek[1] * self.ulamek[1]
        nwd = NWD(a, b)
        return frac(a / nwd, b / nwd)


    def __mul__ (self,other):
        a = self.ulamek[0] * other.ulamek[0]
        b = other.ulamek[1] * self.ulamek[1]
        return frac(a / (NWD(a, b)), b / NWD(a, b))


    def __div__(self,other):
        if other.ulamek[0] == 0:
            raise ValueError("Nie mozna dzielic przez 0")

        else:
            a = self.ulamek[0] * other.ulamek[1]
            b = self.ulamek[1] * other.ulamek[0]
            nwd = NWD(a, b)
            return frac(a / nwd, b / nwd)


    def __cmp__(self, other):
        if isinstance(self.ulamek, list) and isinstance(other, (float, int)):
            a = float(self.ulamek[0]) / float(self.ulamek[1])
            b = other
        elif isinstance(self.ulamek, list) and isinstance(other.ulamek, list):
            a_nwd = NWD(self.ulamek[0], self.ulamek[1])
            a = [self.ulamek[0] / a_nwd, self.ulamek[1] / a_nwd]
            b_nwd = NWD(other.ulamek[0], other.ulamek[1])
            b = [other.ulamek[0] / b_nwd, other.ulamek[1] / b_nwd]
        else:
            raise TypeError

        if a == b:
            return 0
        elif (self.ulamek[0] / self.ulamek[1]) > (other.ulamek[0] / other.ulamek[1]):
            return 1
        elif (self.ulamek[0] / self.ulamek[1]) < (other.ulamek[0] / other.ulamek[1]):
            return -1


    def is_positive(self):
        if self.ulamek [0]/self.ulamek[1] > 0:
            return True
        else:
            return False

    def is_zero(self):
        if self.ulamek[0] == 0:
            return True
        else:
            return False

    def __float__(self):
        return float(self.ulamek[0]) / float(self.ulamek[1])

    def kill(self):
        del self