import matplotlib.pyplot as plt
import math
import numpy as np

# количество итераций
N = 1000
# z[0]
Z = [0.5]
# дельта t
dt = 0.01
K = 1 / dt

t = np.arange(dt, dt+N*dt, dt)
print(f"len t={len(t)}")


def my_func(t):
    return math.sin(t) * math.sin(t) + math.cos(t)


def analitic_df(t):
    return 2*math.sin(t) * math.cos(t) - math.sin(t)


x1 = [my_func(0)]
x2 = [analitic_df(0)]
x3 = []

for i in range(0, len(t)):
    x1.append(my_func(t[i]))
    x2.append(analitic_df(t[i]))

    Z.append(K*dt*(x1[i] - Z[i]) + Z[i])
    x3.append(K*(Z[i+1] - Z[i]))


# extra exs
abs_pogr = []
for i in range(1, len(x3)):
    abs_pogr.append(x2[i] - x3[i])
print("abs_pogr", abs_pogr)
#
# plt.plot(t, x1[1:], 'b', label='X(t)')
plt.plot(t, x2[1:], 'r', label="X'(t)", linestyle='--')
plt.plot(t[1:], x3[1:], 'g', label="K*(X(t)-Z(t))", linestyle=':')

# plt.plot(t[1:], abs_pogr, 'y', label="pogr")
plt.grid(True)
plt.ylabel('x')
plt.xlabel('t')
plt.legend(loc='best')
plt.show()