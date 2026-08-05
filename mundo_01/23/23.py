numero2 = int(input('Digite un número de 0 a 9999: '))

u = numero2 // 1 % 10
d = numero2 // 10 % 10
c = numero2 // 100 % 10
m = numero2 // 1000 % 10

print()
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Unidade de milhar: {m}')