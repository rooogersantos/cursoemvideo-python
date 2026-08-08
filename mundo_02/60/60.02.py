n2 = int(input('Digite um número para calcular seu fatorial: '))
c2 = n2
f2 = 1
print(f'Calculando {n2}! = ', end='')
while c2 > 0:
    print(f'{c2}', end='')
    print(' x ' if c2 > 1 else ' = ', end='')
    f2 = f2 * c2
    c2 -= 1
print(f'{f2}.')