from PIL import Image

def run(path):
    # считывание изображения
    img = Image.open(path)
    obj = img.load()
    # количество строк
    width = img.size[1]
    # количество столбцов
    height = img.size[0]
    print(img.size)
    print(f"string -> {width}  column -> {height}")

    #I Создание матрици энергии
    energy = []

    # интенсивность по rgb
    i_r = []
    i_g = []
    i_b = []

    # считываем интенсивность в списки
    for i in range(width):
        i_r.append([])
        i_g.append([])
        i_b.append([])
        for j in range(height):
            i_r[i].append(obj[j, i][0])
            i_g[i].append(obj[j, i][1])
            i_b[i].append(obj[j, i][2])

    print(i_r)
    print(i_g)
    print(i_b)

    # вычислим энергию для пикселей исключая крайний правый столбец и нижнюю строку
    for i in range(width-1):
        energy.append([])
        for j in range(height-1):
            temp_e_r = round((abs(i_r[i][j] - i_r[i + 1][j]) + abs(i_r[i][j] - i_r[i][j + 1])) / 2)
            temp_e_g = round((abs(i_g[i][j] - i_g[i + 1][j]) + abs(i_g[i][j] - i_g[i][j + 1])) / 2)
            temp_e_b = round((abs(i_b[i][j] - i_b[i + 1][j]) + abs(i_b[i][j] - i_b[i][j + 1])) / 2)
            energy[i].append(temp_e_r + temp_e_g + temp_e_b)

    # посчитаем для крайнего правого столбца
    for i in range(width-1):
        temp_e_r = abs(i_r[i][height - 1] - i_r[i + 1][height - 1])
        temp_e_g = abs(i_g[i][height - 1] - i_g[i + 1][height - 1])
        temp_e_b = abs(i_b[i][height - 1] - i_b[i + 1][height - 1])
        energy[i].append(temp_e_r + temp_e_g + temp_e_b)

    # для нижней строки
    mass = []
    for i in range(height-1):
        temp_e_r = abs(i_r[width - 1][i] - i_r[width - 1][i+1])
        temp_e_g = abs(i_g[width - 1][i] - i_g[width - 1][i+1])
        temp_e_b = abs(i_b[width - 1][i] - i_b[width - 1][i+1])
        mass.append(temp_e_r + temp_e_g + temp_e_b)
    energy.append(mass)

    # элемент в правом нижнем углу равен 0
    energy[width-1].append(0)

    print("energy:", energy)



    #II поиск минимальных швов

    # создадим матрицу сумм
    summ = []

    # первая строка совпадает с первой строкой энергий
    summ.append(energy[0])

    # послудующие вычисляем по правилу: energy[i,j] + MIN ( sum[i-1, j-1], sum[i-1, j], sum[i-1, j+1])
    for i in range(1, width):
        summ.append([])
        for j in range(height):
            temp_list = []
            # элемент сверху всегда есть
            temp_list.append(summ[i-1][j])
            # верхнего левого нет для крайнего левого столбца
            if (j-1 >= 0):
                temp_list.append(summ[i-1][j-1])

            # верхнего правого нет для крайнего правого столбца
            try:
                temp_list.append(summ[i-1][j+1])
            except:
                pass
            summ[i].append(energy[i][j] + min(temp_list))


    print(f"summ: {summ}")

    # обратный проход. Ищем найменьший шов

    # координаты шва
    path = []

    # найдем минимальный элемент в нижней строке
    m = min(summ[width-1])
    # узнаем его индекс
    index = summ[width-1].index(m)
    # now_s = width-1
    # now_c = index
    print(m, index)
    path.append([width-1, index])

    for i in range(width-2, -1, -1):
        temp_list = []
        temp_list.append([summ[i][index], index])

        if index - 1 >= 0:
            temp_list.append([summ[i][index-1], index-1])

        if index + 1 < height-1:
            temp_list.append([summ[i][index+1], index+1])

        m = min(temp_list, key=lambda x: x[0])
        index = m[1]
        path.append([i, index])

    print(f"path: {path}")

    for i in path:
        obj[i[1], i[0]] = (255, 0, 0)
    # img.show()
    img.close()

    #III удаление лишнего шва

    # просто создадим новый файл на основе информации, которую имеем, но пропустим пиксели из шва
    path = sorted(path, key=lambda x:x[0])
    n_img = Image.new("RGB", (height-1, width))
    for i in range(width):
        i_r[i] = i_r[i][0:path[i][1]] + i_r[i][path[i][1] + 1:]
        i_g[i] = i_g[i][0:path[i][1]] + i_g[i][path[i][1] + 1:]
        i_b[i] = i_b[i][0:path[i][1]] + i_b[i][path[i][1] + 1:]
    for i in range(width-1):
        for j in range(height-1):
            n_img.putpixel((j, i), (i_r[i][j], i_g[i][j], i_b[i][j]))

    # n_img.show()
    n_img.save("new_image.png")
    return "new_image.png"

if __name__ == "__main__":
    amount = 100

    temp = run("test3.png")

    for i in range(amount):
        run(temp)