from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from decimal import Decimal, ROUND_HALF_UP
from tkinter import *
from tkinter import filedialog as fd

from_x = -1
from_y = -1
end_x = 1
end_y = 1
path = "data.txt"
v = []
cells = []
step_x = 0
step_y = 0

grid_flag = False

class Cell():
    # x,y,z - списки состоящие из 4х эл-в
    def __init__(self, x, y, z):
        self.x = x[:]
        self.y = y[:]
        self.z = z[:]

    def print_arg(self):
        print(f"x:{self.x}")
        print(f"y:{self.y}")
        print(f"z:{self.z}")
        print()

    def izoline(self, h = 0):
        #строим заданную высоту h

        # посчитаем количество граней где лежит данное значение
        amount = 0
        ansver = []
        # нижняя грань
        if self.z[0] < h < self.z[1] or self.z[1] < h < self.z[0]:
            amount += 1
            t_xb = self.x[0] + (self.x[1] - self.x[0]) * (h - self.z[0]) / (self.z[1] - self.z[0])
            t_yb = self.y[0]
            ansver.append([t_xb, t_yb])

        # левая грань
        if self.z[0] < h < self.z[2] or self.z[2] < h < self.z[0]:
            amount += 1
            t_xl = self.x[0]
            t_yl = self.y[0] + (self.y[2] - self.y[0]) * (h - self.z[0]) / (self.z[2] - self.z[0])
            ansver.append([t_xl, t_yl])

        # правая грань
        if self.z[1] < h < self.z[3] or self.z[3] < h < self.z[1]:
            amount += 1
            t_xr = self.x[1]
            t_yr = self.y[1] + (self.y[3] - self.y[1]) * (h - self.z[1]) / (self.z[3] - self.z[1])
            ansver.append([t_xr, t_yr])

        # верхняя грань
        if self.z[2] < h < self.z[3] or self.z[3] < h < self.z[2]:
            amount += 1
            t_xt = self.x[2] + (self.x[3] - self.x[2]) * (h - self.z[2]) / (self.z[3] - self.z[2])
            t_yt = self.y[2]
            ansver.append([t_xt, t_yt])


            # фиксированный вариант
            # if amount == 4:
            #     # посчитаем x,y для верхней грани в паре с правой и для левой в паре с нижней
            #     # нижняя грань
            #     t_xb = self.x[0] + (self.x[1] - self.x[0])*(h  - self.z[0]) / (self.z[1] - self.z[0])
            #     t_yb = self.y[0]
            #
            #     # верхняя грань
            #     t_xt = self.x[2] + (self.x[3] - self.x[2])*(h  - self.z[2]) / (self.z[3] - self.z[2])
            #     t_yt = self.y[2]
            #
            #     # левая грань
            #     t_xl = self.x[0]
            #     t_yl = self.y[0] + (self.y[2] - self.y[0])*(h  - self.y[0]) / (self.y[2] - self.y[0])
            #
            #     # правая грань
            #     t_xr = self.x[1]
            #     t_yr = self.y[1] + (self.y[3] - self.y[1])*(h  - self.y[1]) / (self.y[3] - self.y[1])
        return ansver

    def draw_izo(self, iz=0, random = False):
        if random == True:
            pass
        #     Zi = z_min + i * (z_mzx - z_min / n ),  где i количество изолиний
        else:
            glColor3f(255.0, 0.0, 0.0)
            glBegin(GL_LINES)
            points = self.izoline(iz)
            for point in points:
                glVertex2f(point[0], point[1])
            glEnd()
            glColor3f(0.0, 0.0, 0.0)

def output(x, y, text):
    glRasterPos2f(x, y)
    # text = 20
    for i in str(text):
        # glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, i)
        # первый аргумент указывает на шрифт, второй это код символа,который выводится
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(i))

def func_x():

    global from_x
    global end_x
    global step_x

    x_min = from_x
    x_max = end_x
    X_max = 0
    X_min = 0

    number = Decimal(np.log10(end_x - from_x)-1)
    number = number.quantize(Decimal("1"), ROUND_HALF_UP)


    k = int(np.log10(end_x - from_x) - 1)
    step = [10 ** k, 2 * pow(10, k), 5 * pow(10, k), pow(10, k + 1), 2 * pow(10, k + 1), 5 * pow(10, k + 1)]
    l = 0

    for el in range(len(step)):
        step[el] = round(step[el])

    if x_min > 0 and x_max > 0:
        while True:
            if abs(x_min) % step[l] != 0:
                X_min = x_min - step[l] - abs(abs(x_min) % step[l])
            else:
                X_min = x_min

            if abs(x_max) % step[l] != 0:
                X_max = x_max + step[l] - abs(abs(x_max) % step[l])
            else:
                X_max = x_max
            if (X_max - X_min) / step[l] > 8:
                l += 1
            else:
                break
    else:
        while True:
            if abs(x_min) % step[l] != 0:
                X_min = x_min - abs(step[l] - abs(abs(x_min) % step[l]))
                print(f"abs(x_min % step[l])  : {abs(abs(x_min) % step[l])}")
            else:
                X_min = x_min
            if abs(x_max) % step[l] != 0:
                X_max = x_max + abs(step[l] - abs(abs(x_max) % step[l]))
            else:
                X_max = x_max
            if (X_max - X_min) / step[l] > 8:
                l += 1
            else:
                break

    from_x = X_min
    end_x = X_max
    step_x = step[l]


def func_y():

    global from_y
    global end_y
    global step_y

    y_min = from_y
    y_max = end_y
    Y_max = 0
    Y_min = 0

    k = int(np.log10(end_y - from_y) - 1)
    step = [10 ** k, 2 * pow(10, k), 5 * pow(10, k), pow(10, k + 1), 2 * pow(10, k + 1), 5 * pow(10, k + 1)]
    l = 0
    for el in range(len(step)):
        step[el] = round(step[el])

    if y_min > 0 and y_max > 0:
        while True:
            if abs(y_min) % step[l] != 0:
                Y_min = y_min - step[l] - abs(abs(y_min) % step[l])
            else:
                Y_min = y_min

            if abs(y_max) % step[l] != 0:
                Y_max = y_max + step[l] - abs(abs(y_max) % step[l])
            else:
                Y_max = y_max
            if (Y_max - Y_min) / step[l] > 8:
                l += 1
            else:
                break
    else:
        while True:
            if abs(y_min) % step[l] != 0:
                Y_min = y_min - abs(step[l] - abs(abs(y_min) % step[l]))
            else:
                Y_min = y_min
            if abs(y_max) % step[l] != 0:
                Y_max = y_max + abs(step[l] - abs(abs(y_max) % step[l]))
            else:
                Y_max = y_max
            if (Y_max - Y_min) / step[l] > 8:
                l += 1
            else:
                break

    from_y = Y_min
    end_y = Y_max
    step_y = step[l]



def drawgrid():
    global from_y
    global end_y
    global step_y
    global from_x
    global end_x
    global step_x
    glBegin(GL_LINES)
    length_x = 0
    length_y = 0
    # сетка
    if grid_flag:
        glColor3f(0, 55, 55)
        for i in np.arange(from_x, end_x+step_x, step_x):
            glVertex2f(i, from_y)
            glVertex2f(i, end_y)
        for i in np.arange(from_y, end_y + step_y, step_y):
            glVertex2f(from_x, i)
            glVertex2f(end_x, i)
        glColor3f(0, 0, 0)

    # рисуем координатные оси
    # горизонталь
    glVertex2f(from_x, from_y)
    glVertex2f(end_x, from_y)
     # засечки по горизонтали

    length_x = pow(10, int(np.log10(abs(end_x - from_x))) - 1)
    length_y = pow(10, int(np.log10(abs(end_y - from_y))) - 1)
    for i in np.arange(from_x, end_x+step_x, step_x):
        glVertex2f(i, from_y + length_y)
        glVertex2f(i, from_y - length_y)
    # вертикаль
    glVertex2f(from_x, from_y)
    glVertex2f(from_x, end_y)
    for i in np.arange(from_y, end_y + step_y, step_y):
        glVertex2f(from_x + length_x, i)
        glVertex2f(from_x - length_x, i)
    glEnd()
    print(f"step_x = {step_x},  step_y = {step_y}")
    for i in np.arange(from_x, end_x + step_x, step_x):
        output(i, from_y - step_y / 2, i)

    for i in np.arange(from_y, end_y + step_y, step_y):
        output(from_x - step_x / 2, i, i)


def figure(v):
    glBegin(GL_LINE_STRIP)
    for i in range(0, len(v)):
        glVertex2d(v[i][0], v[i][1])
    glEnd()


def Draw():
    global v
    # очистка буфера цвета и глубины
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    drawgrid()
    # on for plot function by 2 variables
    h = [-0.5, 0, 0.5]
    for i in h:
        for cell in cells:
            cell.draw_izo(i)
    # on if you will work with izolines
    glutSwapBuffers()


def KeyBoard(key, x, y):
    print("This key have code ", key)
    if key == 27:
        exit(0)
    if key == b'g':
        global grid_flag
        if grid_flag == False:
            grid_flag = True
        else:
            grid_flag = False
        Draw()
    if key == b'o':
        global path
        root = Tk()
        path = fd.askopenfilename()
        print(f"path {path}")
        root.destroy()
        read()
        Initialize()
        Draw()

def Initialize():
    # Выбрать фоновый (очищающий) цвет
    func_x()
    func_y()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(from_x - step_x, end_x + step_x, from_y - step_y, end_y + step_y, -1.0, 1.0)


def Reshape(width,  height):
    func_x()
    func_y()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    lenght = 0
    if width > height:
        lenght = height
    else:
        lenght = width
    glViewport(0, 0, lenght, lenght)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(from_x - step_x, end_x + step_x, from_y - step_y, end_y + step_y, -1.0, 1.0)
    Draw()
    glMatrixMode(GL_MODELVIEW)

def mouseButton(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        print("now i in : x =  ", x,"     y =  ", 600-y )


def read():
    global path
    global from_x
    global from_y
    global end_x
    global end_y
    global v
    v = []
    if path:
        with open(path, "rt") as f:
            lines = f.readlines()
        # strip - удаляет пробельные символы в начале и в конце строки
        lines = [x.strip() for x in lines]
        try:
            long_line = int(lines[0])
        except:
            long_line = 0
        for line in lines:
            tokens = line.split()
            try:
                x, y, z = tokens[0], tokens[1], tokens[2]
                x, y, z = float(x), float(y), float(z)
                v.append([x, y, z])
            except:
                pass
        print(v)
        temp_x = list(map(lambda x: x[0], v))
        temp_y = list(map(lambda x: x[1], v))
        x_min = min(temp_x)
        x_max = max(temp_x)
        y_min = min(temp_y)
        y_max = max(temp_y)
        print(f"x_min = {x_min}, x_max = {x_max}, y_min = {y_min}, y_max = {y_max}")
        from_x = round(x_min) - 1
        end_x = round(x_max) + 1
        from_y = round(y_min) - 1
        end_y = round(y_max) + 1

        # заполняем множество ячеек
        global cells
        temp_signum = 0
        for i in range(len(v) - 1 - long_line):
            if temp_signum == long_line-1:
                temp_signum = 0
                pass
            else:
                cells.append(Cell([v[i][0], v[i + 1][0], v[i + long_line][0], v[i + long_line + 1][0]],
                                  [v[i][1], v[i + 1][1], v[i + long_line][1], v[i + long_line + 1][1]],
                                  [v[i][2], v[i + 1][2], v[i + long_line][2], v[i + long_line + 1][2]]))
                temp_signum += 1
        for c in cells:
            c.print_arg()


    else:
        print("Press 'o' and choose file")
        from_x = -1
        end_x = 1
        from_y = -1
        end_y = 1


if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Gilbert's Curve")
    # Initialize()
    read()
    glutDisplayFunc(Draw)
    glutKeyboardFunc(KeyBoard)
    glutMouseFunc(mouseButton)
    glutReshapeFunc(Reshape)
    glutMainLoop()

