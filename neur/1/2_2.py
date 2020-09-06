import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x / 5.) * np.exp(x / 10.) + 5 * np.exp(-x / 2.)


outFile = open('neur/1/outFile.txt', 'w')
X = np.arange(1, 15, 0.1)
Y = np.array(f(X))
A = np.array(((1, 1, 1, 1), (1, 4, 4 ** 2, 4 ** 3), (1, 10, 10 ** 2, 10 ** 3), (1, 15, 15 ** 2, 15 ** 3)))
B = np.array((f(1), f(4), f(10), f(15)))
C = scipy.linalg.solve(A, B)
print(C[0], C[1], C[2], C[3], end = '', file = outFile)
F = np.array(C[0] + C[1] * X + C[2] * X ** 2 + C[3] * X ** 3)
fig = plt.figure()
graph1 = plt.plot(X, Y)
graph2 = plt.plot(X, F)
grid1 = plt.grid(True)
plt.show()