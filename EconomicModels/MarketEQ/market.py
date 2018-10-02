import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('viridis')
sns.set_context('talk')

#Formulas for market equilibrium
# Pd = a + b*x
# Ps = c + d*x
# a + b*q = c + d*q
# (a-c)/(d-c) = Q*
# P* = a + b*Q*

class Market():
    def __init__(self,da,db,sc,sd):
        self.da = da
        self.db = db
        self.sc = sc
        self.sd = sd

    def inverse_demand(self, x):
        return self.da + self.db * x

    def inverse_supply(self, x):
        return self.sc +self.sd * x

    def equilibrium(self):
        #eq quantity
        Q = (self.da - self.sc) / (self.sd - self.db)
        #eq price
        P = self.da + self.db * Q
        return Q, P

    def consumer_surplus(self):
        q, p = self.equilibrium()
        return( self.da - p) * q / 2

    def producer_surplus(self):
        q, p = self.equilibrium()
        return(p - self.sc) * q / 2

m1 = Market(8, -1, 2, 1)
#x axis is quantity; linspace default is 50
x_axis = np.linspace(0, 12)
pd = m1.inverse_demand(x_axis)
fig, ax = plt.subplots()
ax.plot(x_axis, pd,label='Demand')
ps = m1.inverse_supply(x_axis)
ax.plot(x_axis, ps,label='Supply 1')



q, p = m1.equilibrium()
print('Initial Equilibrium Quantity is:', q)
print('Initial Equilibrium Price is:', p,'\n')

cs = m1.consumer_surplus()
ps = m1.producer_surplus()
print('Initial Consumer Surplus is:', cs)
print('Initial Producer Surplus is:',ps ,'\n')

#NEW MARKET WITH SAME DEMAND but sifferent supply
m2 = Market(8, -1, 3, 1.5)
ps2 = m2.inverse_supply(x_axis)
ax.plot(x_axis, ps2, label='Supply 2')

plt.legend()
plt.show()

q, p = m2.equilibrium()
print('New Equilibrium Quantity is:', q)
print('New Equilibrium Price is:', p,'\n')

cs = m2.consumer_surplus()
ps = m2.producer_surplus()
print('New Consumer Surplus is:', cs)
print('New Producer Surplus is:',ps ,'\n')
