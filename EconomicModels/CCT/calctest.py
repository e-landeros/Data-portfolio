import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize as sp
sns.set_context('talk')
sns.set_palette('Set1')
sns.set_style('darkgrid')
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 5)
f = lambda x: (x-2)**2 + 2
y = f(x)
f2 = lambda x: 0*x
zero_line = f2(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='Quadratic function')
ax.plot(x, zero_line)
plt.ylim(-1,10)
plt.legend()
plt.show()

#minimize 1 var quadaratic function
results = sp.minimize_scalar(f)
print(results)
# fun: 2.0
# nfev: 9
# nit: 4  # 4 itteration to find it
# success: True
# x: 1.9999999999999998

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
x = np.linspace(0,10)
y = np.linspace(0,10)
f = lambda x,y: (x-5)**2 + (y-5)**2 +10
X, Y = np.meshgrid(x,y)
Z = f(X, Y)
ax.plot_surface(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

f_ = lambda x: (x[0]-5)**2 + (x[1]-5)**2 +10
results2 = sp.minimize(f_, [0,10])
print(results2)
