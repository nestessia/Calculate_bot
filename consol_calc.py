from math import sqrt
import math


def task(x: float):
    return x*x+5*x+3

def KratInt(x:float, y:float):
    return math.sin(x+y)

def left(n: int, A:float, B:float):
    h = (B - A) / n
    x = A
    result = 0
    while x <= (B - h):
        result += task(x)
        x += h
    return h * result

def right(n: int, A:float, B:float):
    h = (B - A) / n
    x = A + h
    result = 0
    while x <= B:
        result += task(x)
        x += h
    return h * result

def trapecia(n: int, A:float, B:float):
    h = (B - A) / n
    x = A + h
    result = 0
    while x <= (B - h):
        result += task(x)
        x += h
    return ((task(A) + task(B)) / 2 + result) * h

def parabola(n: int, A:float, B:float):
    h = (B - A) / n
    S1 = 0
    x = A + h
    while x <= (B - h):
        S1 += task(x)
        x += 2 * h
    S2 = 0
    x = A + (2 * h)
    while x <= (B - (2 * h)):
        S2 += task(x)
        x += 2 * h
    return (task(A) + task(B) + (4 * S1) + (2 * S2)) * (h / 3)

def doubleRecalc(e:float, A:float, B:float):
    n = 2
    f1 = 0
    f2 = left(n, A, B)
    while abs(f1-f2) > e:
        f1 = f2
        n = n * 2
        f2 = left(n, A, B)
    return f2

def doubleRecalcBetter(e:float, A:float, B:float):
    n = 2
    otst = (B - A)/2
    f1 = left(n, A, B)
    otst = otst / 2
    f2 = left(n, A + otst, B)
    while abs(f1-f2) > e:
        f1 = f2
        n = n * 2
        otst = otst / 2
        f2 = left(n, A+otst, B)
    return f2

def kratniy(nx:int, ny:int, A:float, B:float, C:float, D:float):
    hx = (B - A) / nx
    hy = (D - C) / ny
    S = 0
    x = A
    while x <= (B - hx):
        y = C
        while y <= (D - hy):
            S += KratInt(x, y)
            y += hy
        x += hx
    return S*hx*hy

def e(x):
    a = [0.9999998, 1.000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
    k = 1
    U = 1.0
    C = a[0]
    P = 1
    e = 2 * math.pow(10, -7)
    x = math.fabs(x)
    while (math.fabs(U) > e):
        P *= x
        U = P * a[k]
        C += U
        if k >= 7:
            break
        else:
            k += 1
    return C

def sin(x):
    a = [1.000000002, -0.166666599, 0.008333075, -0.000198107, 0.000002608]
    k = 1
    U = 1.0
    P = 1
    pi = 3.14
    e = 6 * math.pow(10, -9)
    x = (pi * x) / 180
    C = a[0] * x
    while (math.fabs(U) > e):
        P *= x**2
        U = P * a[k] * x
        C += U
        if k >= 4:
            break
        else:
            k += 1
    return C
def MetodIteraciy1(x:float, y0:float, ebs:float):
    res = y0
    while abs(x-res**2)>ebs:
        res = (1/2)*(res + x / res)
    return res

def MetodIteraciy2(x:float, y0:float, ebs:float):
    res = y0
    while abs(x - (1/res)**2) > ebs:
        res = (res / 2)*(3 - x * res**2)
    return res

def calcEval(f):
    return eval(f)

def Eiler_1_poryadok(x0, y0, a, b, n, f:str, colResh):
    count = 0
    h = (b-a) / n
    x = x0
    y = y0
    while (x < b) and (count < colResh):
        y += h * eval(f)
        x += h
        print('x = ', round(x, 3), '  y = ', round(y, 3))
        count += 1
def Runge_1_poryadok(x0, y0, a, b, n, f:str, colResh):
    count = 0
    h = (b - a) / n
    x = x0
    y = y0
    while (x < b) and (count < colResh):
        xbuffer = x
        ybuffer = y
        k1 = h * eval(f)
        x = xbuffer + h/2
        y = ybuffer + k1/2
        k2 = h * eval(f)
        x = xbuffer + h/2
        y = ybuffer + k2/2
        k3 = h * eval(f)
        x = xbuffer + h
        y = ybuffer + k3
        k4 = h * eval(f)
        F = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y = ybuffer + F
        x = xbuffer + h
        print('x = ', round(x, 3), '  y = ', round(y, 3))
        count += 1

special1 = True
while special1 == True:
    special2 = True
    print("Welcome to MainMenu")
    print("Для выбора задачи нажмите соответствующую кнопку:")
    print('[1]Численное интегрирование\n'
          '[2]Вычисление элементарной функции\n'
          '[3]Численное решение ДУ\n'
          'more will comming soon')
    mean1 = int(input())

    if mean1 == 1:
        while special2 == True:
            special3 = True
            print("Выберите:\n"
                  "[1] С постоянным шагом\n"
                  "[2] С переменным шагом\n"
                  "[3] Кратный интегралл")
            print("Для выхода в меню введите '4'")
            mean2 = int(input())

            if mean2 == 1:
                print("Выбран постоянный шаг\n")
                while special3 == True:
                    print("Выберите метод:\n"
                          "[1] Метод левых прямоугольников\n"
                          "[2] Метод правых прямоугольников\n"
                          "[3] Метод Симпсона(парабол)\n"
                          "[4] Метод трапеций")
                    print("Для возврата нажмите '5'")
                    mean3 = int(input())

                    if mean3 == 1:
                        print("Выбран 'Метод левых прямоугольников'")
                        print('Введите количество разбиений')
                        n = int(input())
                        print('Введите нижнюю границу')
                        A = float(input())
                        print('Введите верхнюю границу')
                        B = float(input())
                        res = left(n, A, B)
                        print("Результат: ", res, '\n')

                    elif mean3 == 2:
                        print("Выбран 'Метод правых прямоугольников'")
                        print('Введите количество разбиений')
                        n = int(input())
                        print('Введите нижнюю границу')
                        A = float(input())
                        print('Введите верхнюю границу')
                        B = float(input())
                        res = right(n, A, B)
                        print("Результат: ", res, '\n')

                    elif mean3 == 3:
                        print("Выбран 'Метод Симпсона(парабол)'")
                        print('Введите количество разбиений')
                        n = int(input())
                        print('Введите нижнюю границу')
                        A = float(input())
                        print('Введите верхнюю границу')
                        B = float(input())
                        res = parabola(n, A, B)
                        print("Результат: ", res, '\n')

                    elif mean3 == 4:
                        print("Выбран 'Метод трапеций'")
                        print('Введите количество разбиений')
                        n = int(input())
                        print('Введите нижнюю границу')
                        A = float(input())
                        print('Введите верхнюю границу')
                        B = float(input())
                        res = trapecia(n, A, B)
                        print("Результат: ", res, '\n')

                    elif mean3 == 5:
                        special3 = False
                        print()

            elif mean2 == 2:
                print("Выбран переменный шаг\n")
                while special3 == True:
                    print("Выберите алгоритм:\n"
                          "[1] Двойной пересчёт алгоритм 1\n"
                          "[2] Двойной пересчёт алгоритм 2")
                    print("Для возврата нажмите '3'")
                    mean4 = int(input())

                    if mean4 == 1:
                        print("Двойной пересчёт'\n"
                              "Алгоритм 1\n"
                              "Метод левых прямоугольников \n")

                        print('Введите точность')
                        e = float(input())
                        print('Введите нижнюю границу')
                        A = float(input())
                        print('Введите верхнюю границу')
                        B = float(input())
                        res = doubleRecalc(e, A, B)
                        print("Результат: ", res, '\n')

                    elif mean4 == 2:
                        print("Двойной пересчёт\n"
                              "Алгоритм 2\n"
                              "Метод левых прямоугольников\n")
                        print('Введите точность')
                        e = float(input())
                        print('Введите нижнюю границу')
                        A = float(input())
                        print('Введите верхнюю границу')
                        B = float(input())
                        res = doubleRecalcBetter(e, A, B)
                        print("Результат: ", res, '\n')

                    elif mean4 == 3:
                        special3 = False
                        print()

            elif mean2 == 3:
                print("Выбран кратный интеграл\n")
                print("Введите количество разбиений по x")
                nx = int(input())
                print("Введите количество разбиений по y")
                ny = int(input())
                print("Введите внешнюю нижнюю границу")
                A = float(input())
                print("Введите внешнюю верхнюю границу")
                B = float(input())
                print("Введите внутреннюю нижнюю границу")
                C = float(input())
                print("Введите внутреннюю верхнюю границу")
                D = float(input())
                res = kratniy(nx, ny, A, B, C, D)
                print("Результат: ", res, '\n')

            elif mean2 == 4:
                special2 = False
    elif mean1 == 2:
        while special2 == True:
            special3 = True
            print("Выберите:\n"
                  "[1] Вычисление показательной функции e^x\n"
                  "[2] Вычисление функции sin(x)\n"
                  "[3] Метод итераций для sqrt(x)\n"
                  "[4] Метод итераций для 1/sqrt(x)")
            print("Для выхода в меню введите '5'")
            mean2 = int(input())

            if mean2 == 1:
                print("Выбрано вычисление показательной функции e^x")
                print("Введите x (x<=1)")
                x = float(input())
                res = e(x)
                print("Результат: ", res, '\n')

            if mean2 == 2:
                print("Выбрано вычисление функции sin(x)")
                print("Введите x в градусах (x <= pi/2)")
                x = float(input())
                res = sin(x)
                print("Результат: ", res, '\n')

            if mean2 == 3:
                print("Выбран метод итераций")
                print("Вычисление sqrt(x)")
                print("Введите x")
                x = float(input())
                print("Введите y0")
                y0 = float(input())
                print("Введите точность")
                ebs = float(input())
                res = MetodIteraciy1(x, y0, ebs)
                print("Результат: ", res, '\n')

            elif mean2 == 4:
                print("Выбран метод итераций")
                print("Вычисление 1/sqrt(x)")
                print("Введите x")
                x = float(input())
                print("Введите y0")
                y0 = float(input())
                print("Введите точность")
                ebs = float(input())
                res = MetodIteraciy2(x, y0, ebs)
                print("Результат: ", res, '\n')

            elif mean2 == 5:
                special2 = False
    elif mean1 == 3:
        while special2 == True:
            special3 = True
            print("Выберите:\n"
                  "[1] Метод Эйлера 1-й порядок\n"
                  "[2] Метод Рунге-Кутта 1-й порядок")
            print("Для выхода в меню введите '3'")
            mean2 = int(input())

            if mean2 == 1:
                print("Выбран 'Метод Эйлера для ДУ 1-го порядка'")
                print("Введите ДУ первого порядка (правую часть выражения)")
                f = str(input())
                print("Введите нижнюю границу отрезка")
                a = float(input())
                print("Введите верхнюю границу отрезка")
                b = float(input())
                print("Введите X0")
                x0 = float(input())
                print("Введите Y0")
                y0 = float(input())
                print("Введите количество разбиений")
                n = int(input())
                print("Введите необходимое количество точек")
                colResh = int(input())
                Eiler_1_poryadok(x0, y0, a, b, n, f, colResh)

            if mean2 == 2:
                print("Выбран 'Метод Рунге-Кутта для ДУ 1-го порядка'")
                print("Введите ДУ первого порядка (правую часть выражения)")
                f = str(input())
                print("Введите нижнюю границу отрезка")
                a = float(input())
                print("Введите верхнюю границу отрезка")
                b = float(input())
                print("Введите X0")
                x0 = float(input())
                print("Введите Y0")
                y0 = float(input())
                print("Введите количество разбиений")
                n = int(input())
                print("Введите необходимое количество точек")
                colResh = int(input())
                Runge_1_poryadok(x0, y0, a, b, n, f, colResh)

            elif mean2 == 3:
                special2 = False