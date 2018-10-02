import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('viridis')
sns.set_context('talk')

# MODELLING A CHANGE IN CONSUMER PREFERENCES

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
ax.plot(x_axis, pd,label='Demand 1')
ps = m1.inverse_supply(x_axis)
ax.plot(x_axis, ps,label='Supply')

#NEW MARKET WITH LARGER DEMAND; demand line shifts upwards
m2 = Market(10, -1, 2, 1)
pd2 = m2.inverse_demand(x_axis)
ax.plot(x_axis, pd2, label='Demand 2')

m3 = Market(12, -1, 2, 1)
pd3 = m3.inverse_demand(x_axis)
ax.plot(x_axis, pd3, label='Demand 3')

m4 = Market(14, -1, 2, 1)
pd4 = m4.inverse_demand(x_axis)
ax.plot(x_axis, pd4, label='Demand 4')

plt.legend()
plt.show()
