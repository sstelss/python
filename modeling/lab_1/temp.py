import numpy as np
import matplotlib.pyplot as plt

N0 = 100
C0 = 6
h_m = np.linspace(0, 10, 101)
# print(h_m)
h = h_m[1] - h_m[0]
fr = 0
to = 2
# h = 0.1


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def dN_dt(N, C):
    return 5 * N - 0.1 * C * N


def dC_dt(N, C, q=2):
    return 0.2 * C * N - q * C

# C - популяция хищника
# N - популяция жертвы



m_f = open('result_euler.txt', 'w')
m_f.write("t                            N(t)               C(t)"+"\n\n")
q_temp = 0.1
while q_temp <= 2:
    N_n = []
    C_n = []
    N_n.append(N0)
    C_n.append(C0)
    k = 0
    m_f.write("For case " + "q = " + str(q_temp) + "\n\n")
    for i in range(len(h_m)-1):
        N_n_plus_1_div_2 = N_n[i] + h/2 * dN_dt(N_n[i], C_n[i])
        C_n_plus_1_div_2 = C_n[i] + h/2 * dC_dt(N_n[i], C_n[i])

        N_n.append(N_n[i] + h * dN_dt(N_n_plus_1_div_2, C_n_plus_1_div_2))
        C_n.append(C_n[i] + h * dC_dt(N_n_plus_1_div_2, C_n_plus_1_div_2))

        s = str(toFixed(k,1)) + "   " * 5 + str(N_n[i]) + "   " * 5 + str(C_n[i]) + "\n"
        m_f.write(s)
        # h += 0.1
        k += h
    m_f.write("\n\n\n")
    plt.plot(h_m, N_n, 'b', label='N(t)- популяция жертвы')
    plt.plot(h_m, C_n, 'g', label='C(t) - популяция хищника')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()

    # plt.show()
    plt.savefig(str(toFixed(q_temp,1)) +"_Euler" + '.png', format='png', dpi=100)
    plt.clf()
    q_temp += 0.1

    del N_n
    del C_n

m_f.close()
