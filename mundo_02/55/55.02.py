maior_peso2 = 0
menor_peso2 = 0

print('=' * 40)
for p in range(1,6):
    peso2 = float(input(f'Digite o peso da {p} pessoa: '))
    print('-' * 40)
    if p == 1:
        maior_peso2 = peso2
        menor_peso2 = peso2
    else:
        if peso2 > maior_peso2:
            maior_peso2 = peso2
        if peso2 < menor_peso2:
            menor_peso2 = peso2

print(f'O maior peso informado é {maior_peso2:.3f}kg.')
print(f'O menor peso informado é {menor_peso2:.3f}kg.')
print('=' * 40)