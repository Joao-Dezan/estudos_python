#!/usr/bin/python3
from functools import reduce

pessoas= [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

# Soma das idades dos menores de idades

idades = map(lambda p: p['idade'], pessoas)
idades_menores = filter(lambda idade: idade < 18, idades)
soma_idades_menores = reduce(lambda idades, idade: idades + idade, idades_menores, 0)

print(soma_idades_menores)
