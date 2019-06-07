import lab2_2 as l

T_o = []
T_p1 = []
T_p2 = []
P_p1 = []
P_p2 = []
for i in range(0, 100):
        t1, t2, t3, t4, t5 = l.run(100)
        T_o.append(t1)
        T_p1.append(t2)
        T_p2.append(t3)
        P_p1.append(t4)
        P_p2.append(t5)

print("\n"*3)
print(f"Среднее для 100 тестов:")
print(f"Ожидание: {sum(T_o)/len(T_o)}")
print(f"Простой первого компуктера: {sum(T_p1)/len(T_p1)}")
print(f"Простой второго компуктера: {sum(T_p2)/len(T_p2)}")
print(f"Вероятность простоя первого компуктера: {sum(P_p1)/len(P_p1)}")
print(f"Вероятность простоя второго компуктера: {sum(P_p2)/len(P_p2)}")
print()