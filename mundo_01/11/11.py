largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
tinta = area/2

print(f'Serão necessários {tinta:.2f}L de tinta para pintar a parede.')