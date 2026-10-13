# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

import random

tupla_aleatorios02 = tuple(random.randint(1, 100) for _ in range(5))
print(f'Os número sorteados foram: {tupla_aleatorios02}')

print(f'O maior número da lista é {max(tupla_aleatorios02)}.')
print(f'O menor número da lista é {min(tupla_aleatorios02)}.')