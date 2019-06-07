import matplotlib.pyplot as plt
import math
import numpy as np

m = 1
v = []
vx = []
vy = []
x = []
y = []

alpha = (45 * math.pi) / 180  # угол
# начальная скорость
v.append(10)
vx.append(v[0] * math.cos(alpha))
vy.append(v[0] * math.sin(alpha))
x.append(0)
y.append(0)
# print(vx)
# print(vy)

# динамическая вязкость среды для воздуха 1
mu = 0.0182
# mu = 1.002 # вода 2
r = 0.190
# формула Стокса
k1 = 6 * math.pi * mu * r
c = 1.11  # безразмерный коэфициент сопротивления
Rho = 1.29  # воздух 1
# Rho = 997 #вода 2
S = math.pi * r * r  # площадь поперечного сечения
k2 = (1 / 2) * c * S * Rho
# шаг
h = 0.001
#
i = 0
# для случая в вакууме 3
k1 = 0; k2 =0
while (y[i] >= 0):
    i += 1
    vx1 = vx[i - 1] + (h / 2) * (
                -h * vx[i - 1] * ((k1 + k2 * math.sqrt(vx[i - 1] * vx[i - 1] + vy[i - 1] * vy[i - 1])) / m))
    vy1 = vy[i - 1] + (h / 2) * (
                -h * vy[i - 1] * ((k1 + k2 * math.sqrt(vx[i - 1] * vx[i - 1] + vy[i - 1] * vy[i - 1])) / m))
    vx.append(vx[i - 1] - h * vx1 * ((k1 + k2 * math.sqrt(vx1 * vx1 + vy1 * vy1)) / m))
    vy.append(vy[i - 1] - 9.80665 * h - h * vy1 * ((k1 + k2 * math.sqrt(vx1 * vx1 + vy1 * vy1)) / m))
    x.append(x[i - 1] + vx[i] * h)
    y.append(y[i - 1] + vy[i] * h)


# print(y)
# print('Vx :', vx)
# print('Vy:', vy)
print("Максимальная высота:", max(y))
print("Длина пройденная при полете", max(x))
plt.plot(x, y, 'r', label='Премещение')
plt.title('Камень')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.legend(loc='best')
# plt.savefig('Air_move.png', format='png', dpi=100)
plt.show()

plt.plot(range(len(vy)), vy, 'g', label='Vx')
plt.plot(range(len(vx)), vx, 'r', label='Vy')
plt.title('Камень скорость')
plt.ylabel('VY')
plt.xlabel('VX')
plt.grid(True)
plt.legend(loc='best')
# plt.savefig('Air_speed.png', format='png', dpi=100)
plt.show()

del vx
del vy
del x
del y