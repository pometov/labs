import math


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def read_number(str):
    number = input(str)
    while not is_float(number):
        number = input("Введите корректное число: ")
    return float(number)


def compare(a, b):
    if a < b:
        return '<'
    elif a > b:
        return '>'
    else:
        return '='

x = read_number("Ввердите x:")
Z1 = (math.cos(x)+math.cos(2*x)+math.cos(6*x)+math.cos(7*x))
Z2 = (4*math.cos(x/2)*math.cos(5/2*x)*math.cos(4*x))
print("Z1 " + compare(Z1, Z2) + " Z2")
