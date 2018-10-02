"""
Production Possibility Frontier:
The PPF indicates the production possibilities of two commodities when resources are fixed.
This means that the production of one commodity can only increase when the production of the other commodity is reduced,
due to the availability of resources. Therefore, the PPF measures the efficiency in which two commodities can be produced together.

"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('talk')
sns.set_palette('Set1')
sns.set_style('darkgrid')


class PPF():
    def __init__(self, max, power_x, power_y):
        """ Initial Parameters """
        self.max = max
        self.power_x = power_x
        self.power_y = power_y

    def frontier(self, X):
        """ The math circle function: cons^2 = x^2 + y^2; x,y>0 """
        #solve for y
        return (self.max**2 - X**self.power_x) ** (1/self.power_y)

    def X_intercept(self):
        """ The math circle function: cons^2 = x^2 + y^2; x,y>0 """
        return ( self.max**2 ) ** (1/self.power_x)

#example comparing 2 countries
ppf1 = PPF(8, 2, 2)
#default value 50 linear spaced points from 0-8
x_axis = np.linspace(0,8)
y_axis = ppf1.frontier(x_axis)
fig, ax = plt.subplots()
ax.plot(x_axis, y_axis, label='Economy 1 - few resources')



#more resources ppf grows
ppf2 = PPF(11, 2, 2)
x_axis2 = np.linspace(0, 10)
y_axis2 = ppf2.frontier(x_axis2)
ax.plot(x_axis2, y_axis2, label='Economy 2 - more resources')

#modifying power of y to show technological advancement
ppf3 = PPF(8, 2, 1.8)
x_axis3 = np.linspace(0, 8)
y_axis3 = ppf3.frontier(x_axis3)
ax.plot(x_axis3, y_axis3, label='Economy 1 - Tech. Advancement')

#this economy has competitive advantage in the production of y units
ppf4 = PPF(9, 2.2, 1.7)
x_axis4 = np.linspace(0, 9)
y_axis4 = ppf4.frontier(x_axis4)
ax.plot(x_axis4, y_axis4, label='Economy 4')

plt.legend()
plt.show()
