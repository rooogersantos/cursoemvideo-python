from math import factorial
n3 = int(input('Digite um número para calcular seu fatorial: '))
c3 = n3

print(f'Calculando {n3}! = ', end='')
while c3 > 0:
    print(f'{c3}', end='')
    print(' x ' if c3 > 1 else ' = ', end='')
    f3 = factorial(n3)
    c3 -= 1
print(f'{f3}.')