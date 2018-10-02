"""
Consumer Choice Theory models :
 preferences to consumption expenditures and to consumer demand curves.
 It analyzes how consumers maximize the desirability of their consumption as
 measured by their preferences subject to limitations on their expenditures,
 by maximizing utility subject to a consumer budget constraint
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize as sp
sns.set_context('talk')
sns.set_palette('Set1')
sns.set_style('darkgrid')
from mpl_toolkits.mplot3d import Axes3D

class Consumer():
    def __init__(self, utility, power_x, power_y, Px, Py):
        self.utility = utility
        self.power_x = power_x
        self.power_y = power_y
        self.Px = Px
        self.Py = Py
#return y value for every x value using C-D func
    def indifference_curve(self, X):
        """ Use Cobb-Douglas function U = X^a * Y^b """
        return (self.utility/ X**self.power_x) ** (1/self.power_y)

    def equilibrium(self, X, Y):
        """ Maximize utility s.t Budget Constraint or Dual """
        # f -> M = pxX + pyY
        f = lambda x: self.Px * x[0] + self.Py * x[1]
        #U = X^a * Y^b ->  U - (X^a * Y^b)
        constr = {'type':'eq','fun': lambda x : self.utility - (x[0]**self.power_x * x[1]**self.power_y)}
        results = sp.minimize(f, [0,10],constraints=constr)
        return results.x, self.Px*results.x[0] + self.Py*results.x[1]

    def budget_constraint(self, X, Y):
        """ Solve for Y in M = pxX + pyY """
        return (self.equilibrium(X, Y)[1] - self.Px * X) / self.Py

consumer1 = Consumer(25, 1, 1, 1, 1)
x = np.linspace(1,10)
y = consumer1.indifference_curve(x)
# solve for equilibrium
basket, M =  consumer1.equilibrium(x, y)
print(basket)
print(M)
#budget constraints
bc = consumer1.budget_constraint(x, y)


#2nd consumer
consumer2 = Consumer(45, 1, 1, 1, 1)
y2 = consumer2.indifference_curve(x)
basket, M =  consumer2.equilibrium(x, y)
bc2 = consumer2.budget_constraint(x, y)


fig, ax = plt.subplots()
ax.plot(x, y, label='Indif. Curve A')
ax.plot(x, bc, label='Budget Constraint A')

ax.plot(x, y2, label='Indif. Curve B')
ax.plot(x, bc2, label='Budget Constraint B')

plt.legend()
plt.show()
