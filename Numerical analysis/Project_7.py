from random import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interpld

#plot definition
x = range(1,11)
x = np.linspace(0,10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f = interpld(x,y)
f2 = interpld(x,y,kind='cubic')
xnew = np.linspace(0,10, num=41, endpoint=True)
plt.plot(x,y,'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()


#plot generation
y = [random() for i in range(0,10)]
n = x.__len__()
A = [[0 for x in range(4)] for y in range(n)]
B = [[0 for x in range(4)] for y in range(n)]
C = [[0 for x in range(4)] for y in range(n)]
D = [[0 for x in range(4)] for y in range(n)]
S = [[0 for x in range(4)] for y in range(n)]
for j in range(1, n):
    A[j - 1] = [0, 0, -1, x * (j + 1)]
    B[j - 1] = [0, 0, -1, x * j]
    D1 = 1
    C1 = 1

    for i in range(1, 4):
        C1 = np.convolve(C1, [A[j - 1][2], A[j - 1][3]])
        D1 = np.convolve(D1, [B[j - 1][2], B[j - 1][3]])
    C[j-1] = (C1-A[j-1]) * (np.power((x*(j+1) - x*j),2))/6
    D[j-1] = (D1-B[j-1])/6
    AA = np.zeros((n, n))
    BB = np.transpose(np.zeros((n, n)))

    for i in range(2, n):
        if i - 1 != 1:
            AA[i-1][i-2] = x * i - x * (i - 1)
        AA[i-1][i-1] = 2 * (x * (i + 1) - x * (i - 1))
        if i + 1 != n:
            AA[i-1][i] = x * (i + 1) - x * i
        BB[i-1] = 6 * (((y*(i + 1) - y*i)/(x*(i + 1) - x*i)) - ((y*i-y*(i - 1))/(x*i- x*(i - 1))))
    ypp = np.zeros((n, n))
    print (len(AA[1:n][1:n]))
    ypp[1:n] = AA[1:n][1:n] / BB[1:n]

for j in range(1, n):
    S[j-1] = A[j-1] * y * j + B[j-1] * y *(j+1)+ C[j-1] * ypp * j + D[j-1] * ypp *(j+1)

for i in range(1, n):
    X = np.linespace(i, i+1, 100)
    Y = S[i-1][0] * np.power(X,3) + S[i-1][1] * np.power(X,2) + S[i-1][2] * X + S[i-1][3]
    plt.figure(1)
    plt.plot(X,Y)
    plt.hold(True)
plt.plot(x,y,'r.')
plt.hold(False)
