metros = float(input('Digite a medida em metros: '))
cm = metros * 100
mm = metros * 1000
km = metros / 1000

print(f'Valor em centímetros: {cm:.0f}cm')
print(f'Valor em milímetros: {mm:.0f}mm')
print(f'Valor em milímetros: {km:.3f}km')