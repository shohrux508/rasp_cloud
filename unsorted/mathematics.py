import math


def factorial(x):
    if x == 0:
        return 1
    else:
        return x* factorial(x-1)


def S(x):
    n = int(input('Введите чёртов n: '))
    sum = 0
    for i in range(1, n):
        solve = float(((-1)**i)*(((2*x)**2*i))/factorial((2*i)))
        sum = sum + solve
    print(f"Оканчательный ответ этой функции с аргументом x={x} и n={n} равна: {sum}")
    

def Y(x):
    cos2 = math.cos(x)
    cos2 = cos2**2
    solution = cos2 - 1
    print(f"Оканчательный ответ этой функции с аргументом {x} равна: {solution*2}")

S(5)
Y(5)



