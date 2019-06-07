from decimal import Decimal
import math as m

long_line = 10
with open("data.txt", "w") as dat:
    print(f"{long_line}", file=dat)

    for i in range(1, long_line+1):
        for j in range(1, long_line+1):
            print(f"{j} {i} {m.cos(j) * m.sin(i)}", file=dat)