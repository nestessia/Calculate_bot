import math

def e():
    a = [0.9999998, 1.000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
    k = 1
    U = 1.0
    C = a[0]
    P = 1
    e = 2 * math.pow(10, -7)
    x = float((input('Введите x (x <= 1): ')))
    x = math.fabs(x)
    while (math.fabs(U) > e):
        P *= x
        U = P * a[k]
        C += U
        if k >= 7:
            break
        else:
            k += 1
    print(C)

e()
