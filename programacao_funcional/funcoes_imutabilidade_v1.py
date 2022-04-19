#!/usr/bin/python3
from functools import reduce
from operator import add

# Duas maneiras de se trabalhar com listas
# -- A Mutável [m]
# Altera os valores do objeto

# -- A Imutável [i]
# Retorna um novo objeto, sem alterar o original

valores = [30, 10, 25, 70, 100, 40]


print(sorted(valores)) # i

#valores.sort() # m
#print(valores)


print(min(valores)) # i
print(max(valores)) # i
print(sum(valores)) # i
print(reduce(add, valores)) # i
print(list(reversed(valores))) # i
#print(valores.reverse()) # m
