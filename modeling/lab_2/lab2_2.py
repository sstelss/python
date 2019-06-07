import random
import numpy as np


def run(N):
# N = 100
    T_prih = [0]
    T_ozid = np.zeros(N)

    T_prostoia1 = 0
    T_prostoia2 = 0
    kol_prost1 = 0
    kol_prost2 = 0


    i = 1
    while i < N:
        T_prih.append(T_prih[i-1] + random.randint(1, 11))
        i += 1
    print(T_prih)

    # первый свободен
    S1 = True
    # второй свободен
    S2 = True

    svoboda1 = -1
    svoboda2 = -1
    ochered = []
    for t in range(0, T_prih[-1]):
        # проверка на освождение
        if t == svoboda1:
            S1 = True
        if t == svoboda2:
            S2 = True

        # проверка очереди
        if S1 and S2:
            if len(ochered) >= 2:
                S1 = False
                S2 = False
                svoboda1 = t + random.randint(1, 20)
                svoboda2 = t + random.randint(1, 19)
                ochered.pop(0)
                ochered.pop(0)
        elif S1:
            if len(ochered) >= 1:
                S1 = False
                svoboda1 = t + random.randint(1, 20)
                ochered.pop(0)
        elif S2:
            if len(ochered) >= 1:
                S2 = False
                svoboda2 = t + random.randint(1, 19)
                ochered.pop(0)

        # увеличение времени ожидания
        for i in ochered:
            T_ozid[i] += 1

        # если это время прихода заявки
        if t in T_prih:
            # если оба свободны
            if S1 and S2:
                if random.random() <= 0.5:
                    S1 = False
                    svoboda1 = t + random.randint(1, 20)
                else:
                    S2 = False
                    svoboda2 = t + random.randint(1, 19)
            elif S1:
                S1 = False
                svoboda1 = t + random.randint(1, 20)
            elif S2:
                S2 = False
                svoboda2 = t + random.randint(1, 19)
            else:
                # первый индекс в глобальной очереди второе время простоя
                ochered.append(T_prih.index(t))
                T_ozid[T_prih.index(t)] += 1

        # увеличение времени простоя
        if S1:
            T_prostoia1 += 1
            kol_prost1 += 1
        if S2:
            T_prostoia2 += 1
            kol_prost2 += 1

    T_ozid = sorted(T_ozid, reverse=True)
    t_o_sr = sum(T_ozid)
    t_o_sr = t_o_sr / (len(T_ozid[:T_ozid.index(0)]))
    print(T_ozid)
    print("Среднее время ожидания", t_o_sr)
    print(f"Prostoy1 = {T_prostoia1};    Prostoy2 = {T_prostoia2}")
    print(f"Prostoy_sred1 = {T_prostoia1/N};    Prostoy_sred2 = {T_prostoia2/N}")
    print(f"Вероятность простоя компьютера1: {kol_prost1/sum(T_ozid)}   компьютера2: {kol_prost2/sum(T_ozid)}")
    return t_o_sr, T_prostoia1/N, T_prostoia2/N, kol_prost1/sum(T_ozid), kol_prost2/sum(T_ozid)

if __name__ == "__main__":
    run(100)