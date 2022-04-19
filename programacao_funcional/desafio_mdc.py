#/usr/bin/python3
from functools import reduce


def e_divisor_comum(numeros, divisor):
    return reduce(lambda e_mdc, numero: e_mdc + (numero % divisor), numeros, 0) == 0


def mdc(numeros):
    for divisor in range(min(numeros), 0, -1):
        if e_divisor_comum(numeros, divisor):
            return divisor

if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
