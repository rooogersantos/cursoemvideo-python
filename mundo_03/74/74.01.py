# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

import random
maior = menor = 0

tupla_aleatorios = tuple(random.randint(1, 100) for _ in range(5))
print(tupla_aleatorios)

for a in range (0, len(tupla_aleatorios)):
    if maior < tupla_aleatorios[a]:
        maior = tupla_aleatorios[a]

menor = tupla_aleatorios[0]
for a in range (1, len(tupla_aleatorios)):
    if menor > tupla_aleatorios[a]:
        menor = tupla_aleatorios[a]

print(f'O maior número da lista é {maior}.')
print(f'O menor número da lista é {menor}.')