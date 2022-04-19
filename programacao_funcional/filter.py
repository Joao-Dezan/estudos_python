#!/usr/bin/python3

pessoas= [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

# Nome dos menores de idade

menores = filter(lambda pessoa: pessoa['idade'] < 18, pessoas)
nomes_menores = map(lambda pessoa: pessoa['nome'], menores)

print(list(nomes_menores))


# Pessoa com nomes grandes (maior que 6 caracteres)

nomes_grandes = filter(lambda pessoa: len(pessoa['nome']) > 6, pessoas)

print(list(nomes_grandes))

