import math
def sin():
    a = [1.000000002, -0.166666599, 0.008333075, -0.000198107, 0.000002608]
    k = 1
    U = 1.0
    P = 1
    pi = 3.14
    e = 6 * math.pow(10, -9)
    x = float((input('Введите x (x <= pi/2): ')))
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
    print(C) #0.7068251795735713

sin()