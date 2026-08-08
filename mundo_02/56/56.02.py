print('Informe os dados do grupo: ')

soma_idades3 = 0
nome_mais_velho3 = 0
idade_mais_velho3 = 0
menos_20 = 0

for i in range(0,4):
    print(f'----- {i+1}ª PESSOA -----')
    nome3 = input('Nome: ').strip()
    idade3 = int(input('Idade: '))
    sexo3 = input('Sexo([F/M]): ').upper().strip()
    if sexo3 != 'F' and sexo3 != 'M':
        sexo3 = input('Inválido. Digite nomente o sexo([F/M]): ').upper().strip()
    soma_idades3 += idade3
    if sexo3 == 'M' and i == 1:
        idade_mais_velho3 = idade3
        nome_mais_velho3 = nome3
    if sexo3 == 'M' and idade_mais_velho3 < idade3:
        idade_mais_velho3 = idade3
        nome_mais_velho3 = nome3
    if sexo3 == 'F' and idade3 < 20:
        menos_20 += 1

idade_media3 = soma_idades3 / 4
print('=' * 50)
print(f'A média das idades informadas é de {idade_media3:.2f} anos.')
print(f'O homem mais velho do grupo é {nome_mais_velho3}, com {idade_mais_velho3} anos.')
if menos_20 == 1:
    print(f'Há {menos_20} mulher com menos de 20 anos nesse grupo.')
else:
    print(f'Há {menos_20} mulheres com menos de 20 anos nesse grupo.')
print('=' * 50)