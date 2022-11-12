from math import sqrt
from math import sin

def task(x: float):
    return x*x+5*x+3

def KratInt(x:float, y:float):
    return sin(x+y)

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



special1 = True
while special1 == True:
    special2 = True
    print("Welcome to MainMenu")
    print("Для выбора задачи нажмите соответствующую кнопку:")
    print('[1]Численное интегрирование\n'
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
                print("Результат",res,'\n')

            elif mean2 == 4:
                special2 = False