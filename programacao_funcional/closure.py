#!/usr/bin/python3
def multiplicar(x):
    def calcular(y):
        return x * y

    return calcular


if __name__ == '__main__':
    mult = multiplicar(2)(3)
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)
    print(f'O dobro de 5 é {dobro(5)}')
    print(f'O triplo de 7 é {triplo(7)}')
    print(mult)