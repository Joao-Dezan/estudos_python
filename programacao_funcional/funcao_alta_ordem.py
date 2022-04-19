#!/usr/bin/python3
from funcao_primeira_classe import dobro, quadrado


def processar(titulo, lista, funcao):
    if not callable(funcao):
        return print('Funcao is not callable')

    print(f'Processando: {titulo}')

    for i in lista:
        print(i, '=>', funcao(i))


processar('Dobro de 10 números', range(1, 11), dobro)
processar('Quadrado de 10 números', range(1, 11), quadrado)