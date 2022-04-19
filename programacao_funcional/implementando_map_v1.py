#!/usr/bin/python3
# Implementação simplificada do map
def mapear(funcao, lista):
    for item in lista:
        yield funcao(item)


if __name__ == '__main__':
    users = [
        {'username': 'joao'},
        {'username': 'admin'}
    ]

    print(mapear(lambda x: x['username'], users))
    print(list(mapear(lambda x: x**2, [4, 2, 6, 2])))
