nome = input('Digite um nome completo: ').strip()
print()

print(f'Apenas maiúsculas {nome.upper()}.')
print(f'Apenas minúsculas {nome.lower()}.')
print()
print(f'O nome completo contém {format(len(nome)-nome.count(' '))} letras.')
print()
print(f'Seu primeiro nome tem {nome.find(' ')} letras.')