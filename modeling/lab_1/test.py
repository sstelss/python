import scipy.integrate as od
import numpy as np
import matplotlib.pyplot as plt

# функция для scipy
def pend(y, t, q, r, a, f):
    # Y является списком переменных которые мы ищем
    N, C = y
    # первый элемент соответствует первому уровнению и так далее
    dydt = [r * N - a * C * N, f * a * C * N - q * C]
    return dydt


# функция для отсечения лишних знаков после запятой numObj-число, digits-сколько знаков должно остаться
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

# начальные параметры
r = 5.0
a = 0.1
f = 2.0
# список на 0 шаге
y0 = [100.0, 6.0]

# задача состоит в оценке решений для 0.1 < q < 2 создаем список содержащий спектр вариации q
q_arr = np.linspace(0.1, 2, 20)
# промежуток по времени на котором производится оценка
t = np.linspace(0, 10, 101)
# переменная указывающая на номер теста(для сохранения картинок)
temp = 1

# создаем текстовый файл с численным результатом для каждого теста
m_f = open('result_sci.txt', 'w')
m_f.write("t                            N(t)               C(t)"+"\n\n")
# производим анализ для каждого q
for q in q_arr:
    # функция scipy
    sol = od.odeint(pend, y0, t, args=(q, r, a, f))
    # номер случая в текстовом файле
    m_f.write("For case " + str(temp) + "\n\n")
    # записываем значения переменных
    for i in range(len(t)):
        t[i] = toFixed(t[i], 1)
        s = str(t[i]) + "   "*5 + str(sol[i, 0]) + "   "*5 + str(sol[i, 1]) + "\n"
        m_f.write(s)
        # print(t[i], "   ", sol[i, 0], "   ", sol[i, 1])
    m_f.write("\n\n\n")

    # производим построение изображения и сохраняем его в текущую папку без отображения на экран
    plt.plot(t, sol[:, 0], 'b', label='N(t)')
    plt.plot(t, sol[:, 1], 'g', label='C(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    # plt.show()
    plt.savefig(str(temp) + "_SciPy" + '.png', format='png', dpi=100)
    plt.clf()
    temp += 1
m_f.close()

print("Done")