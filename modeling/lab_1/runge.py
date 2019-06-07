import numpy as np
import matplotlib.pyplot as plt

# см пояснения в Eulier
N0 = 100
C0 = 6
h_m = np.linspace(0, 10, 101)
fr = 0
to = 2
h = h_m[1]-h_m[0]

def dN_dt(N, C):
    return 5 * N - 0.1 * C * N


def dC_dt(N, C, q=2):
    return 0.2 * C * N - q * C


def d_four(N, C):
    k1 = h * dN_dt(N, C)
    l1 = h * dC_dt(N, C)

    k2 = h * dN_dt(N + k1 / 2, C + l1 / 2)
    l2 = h * dC_dt(N + k1 / 2, C + l1 / 2)

    k3 = h * dN_dt(N + k2 / 2, C + l2 / 2)
    l3 = h * dC_dt(N + k2 / 2, C + l2 / 2)

    k4 = h * dN_dt(N + k3, C + l3)
    l4 = h * dC_dt(N + k3, C + l3)

    dN = (k1 +2*k2 + 2*k3 + k4) / 6
    dC =(l1 +2*l2 + 2*l3 + l4) / 6
    return dN, dC

N = [N0]
C = [C0]
t = 0
print(N, " "*10, C)
for i in range(len(h_m)-1):
    dN, dC = d_four(N[i], C[i])
    N.append(N[i] + dN)
    C.append(C[i] + dC)
    print(t, N[i], " "*10, C[i])
    t += h

plt.plot(h_m, N, 'b', label='N(t)- популяция жертвы')
plt.plot(h_m, C, 'g', label='C(t) - популяция хищника')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()

plt.show()


