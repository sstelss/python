import numpy as np
import matplotlib.pyplot as plt

# начальные значения для варианта 17
N0 = 100
C0 = 6
# массив шагов для построения графика
h_m = np.linspace(0, 10, 100)
# шаг
h = h_m[1] - h_m[0]

# функция для отсечения лишних знаков после запятой numObj-число, digits-сколько знаков должно остаться
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

# функция для жертв
def dN_dt(N, C):
    return 5 * N - 0.1 * C * N

# функция для хищников
def dC_dt(N, C, q=2.0):
    return 0.2 * C * N - q * C

# C - популяция хищника
# N - популяция жертвы
N_n = []
C_n = []
N_n.append(N0)
C_n.append(C0)

k = 0
for i in range(len(h_m)-1):
    # вычисляем значение на шаге i+1/2
    N_n_plus_1_div_2 = N_n[i] + h/2 * dN_dt(N_n[i], C_n[i])
    C_n_plus_1_div_2 = C_n[i] + h/2 * dC_dt(N_n[i], C_n[i])
    # на шаге i+1
    N_n.append(N_n[i] + h * dN_dt(N_n_plus_1_div_2, C_n_plus_1_div_2))
    C_n.append(C_n[i] + h * dC_dt(N_n_plus_1_div_2, C_n_plus_1_div_2))
    print( toFixed(k,1), " "*15, N_n[i], " "*15, C_n[i])
    k += h

plt.plot(h_m, N_n, 'b', label='N(t)- популяция жертвы')
plt.plot(h_m, C_n, 'g', label='C(t) - популяция хищника')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()

plt.show()
