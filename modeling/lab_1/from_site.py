from numpy import *
import pylab as p
from scipy import integrate

# Definition of parameters
# a = 1.  #r
# b = 0.1  #a
# c = 1.5  #q
# d = 0.75  #f
a = 5.  #r
b = 0.1  #a
c = 2  #q
d = 2  #f
def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return array([ a*X[0] - b*X[0]*X[1],
                  -c*X[1] + d*b*X[0]*X[1] ])


t = linspace(0, 15,  100)              # time
X0 = array([100, 6])                     # initials conditions: 10 rabbits and 5 foxes

X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
infodict['message']                     # >>> 'Integration successful.'
print(X.T)

rabbits, foxes = X.T

f1 = p.figure()
p.plot(t, rabbits, 'r-', label='Rabbits')
p.plot(t, foxes  , 'b-', label='Foxes')
p.grid()
p.legend(loc='best')
p.xlabel('time')
p.ylabel('population')
p.title('Evolution of fox and rabbit populations')
# f1.savefig('rabbits_and_foxes_1.png')
p.show()