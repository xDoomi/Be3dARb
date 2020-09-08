import numpy as np
import scipy.optimize
import math
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)


def h(x):
    return int(f(x))


################1задание################
#print(scipy.optimize.minimize(f, 2, method='BFGS'), scipy.optimize.minimize(f, 30, method='BFGS'))
################2задание################
#print(scipy.optimize.differential_evolution(f, [(1, 30)]))
################3задание################
print(scipy.optimize.minimize(h, 30, method='BFGS'), scipy.optimize.differential_evolution(h, [(1,30)])) 
X = np.arange(1, 30, 0.1)
Y = np.vectorize(h)
fig = plt.figure()
graph1 = plt.plot(X, Y(X))
grid1 = plt.grid(True)
plt.show()