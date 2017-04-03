
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import math

# define objective function
def f(x):
    x1 = x[0]
    x2 = x[1]
    obj = 0.2 + x1**2 + x2**2 - 0.1*math.cos(6.0*3.1415*x1) - 0.1*math.cos(6.0*3.1415*x2)
    return obj

# Start location
x_start = [0.8, -0.5]


i1 = np.arange(-1.0, 1.0, 0.01)
i2 = np.arange(-1.0, 1.0, 0.01)
x1m, x2m = np.meshgrid(i1, i2)
fm = np.zeros(x1m.shape)
for i in range(x1m.shape[0]):
    for j in range(x1m.shape[1]):
        fm[i][j] = 0.2 + x1m[i][j]**2 + x2m[i][j]**2 \
             - 0.1*math.cos(6.0*3.1415*x1m[i][j]) \
             - 0.1*math.cos(6.0*3.1415*x2m[i][j])


plt.figure()
CS = plt.contour(x1m, x2m, fm)#,lines)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Non-Convex Function')
plt.xlabel('x1')
plt.ylabel('x2')

n = 50
m = 50
na = 0.0
p1 = 0.7
p50 = 0.001
t1 = -1.0/math.log(p1)
t50 = -1.0/math.log(p50)
frac = (t50/t1)**(1.0/(n-1.0))
x = np.zeros((n+1,2))
x[0] = x_start
xi = np.zeros(2)
xi = x_start
na = na + 1.0

xc = np.zeros(2)
xc = x[0]
fc = f(xi)
fs = np.zeros(n+1)
fs[0] = fc
t = t1


DeltaE_avg = 0.0
for i in range(n):
    print 'Cycle: ' + str(i) + ' with Temperature: ' + str(t)
    for j in range(m):
        xi[0] = xc[0] + random.random() - 0.5
        xi[1] = xc[1] + random.random() - 0.5
        # Clip to upper and lower bounds
        xi[0] = max(min(xi[0],1.0),-1.0)
        xi[1] = max(min(xi[1],1.0),-1.0)
        DeltaE = abs(f(xi)-fc)
        if (f(xi)>fc):
            if (i==0 and j==0): DeltaE_avg = DeltaE
            p = math.exp(-DeltaE/(DeltaE_avg * t))
            if (random.random()<p):
                # accept the worse solution
                accept = True
            else:
                # don't accept the worse solution
                accept = False
        else:
            accept = True
        if (accept==True):
            xc[0] = xi[0]
            xc[1] = xi[1]
            fc = f(xc)
            na = na + 1.0
            DeltaE_avg = (DeltaE_avg * (na-1.0) +  DeltaE) / na

    # Record the best x values at the end of every cycle
    x[i+1][0] = xc[0]
    x[i+1][1] = xc[1]
    fs[i+1] = fc
    t = frac * t

# print solution
print 'Best solution: ' + str(xc)
print 'Best objective: ' + str(fc)

plt.plot(x[:,0],x[:,1],'y-o')
plt.savefig('contour.png')

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(fs,'r.-')
ax1.legend(['Objective'])
ax2 = fig.add_subplot(212)
ax2.plot(x[:,0],'b.-')
ax2.plot(x[:,1],'g--')
ax2.legend(['x1','x2'])

# Save the figure as a PNG
plt.savefig('iterations.png')

plt.show()
