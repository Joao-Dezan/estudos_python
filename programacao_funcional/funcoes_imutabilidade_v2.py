#!/usr/bin/python3
from functools import reduce
from operator import add

# Preferir usar estruturas de dados imutáveis
# Quando se trabalhar com imutabilidade

valores = (30, 10, 25, 70, 100, 40)

print(sorted(valores))
print(min(valores)) 
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(tuple(reversed(valores))) 
