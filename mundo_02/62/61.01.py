print(f'Vamos criar uma Progressão Aritmética com 10 termos.')
primeiro2 = int(input('Digite o primeiro número da PA: '))
razao2 = int(input('Digite a razão da PA: '))
operacao2 = 1
termo2 = primeiro2
quantidade2 = 1
print(f'{termo2}', end=' - ')

while operacao2 < 10:
    termo2 = termo2 + razao2
    print(f'{termo2}', end=' - ')
    operacao2 += 1
    quantidade2 += 1
print(f'PAUSA')
print()
continua2 = input('Deseja ver mais termos? [S/N]: ').upper()

if continua2 not in 'SN':
    print('Opção Inválida!')
    continua2 = input('Deseja ver mais termos? [S/N]: ').upper()  

while continua2 == 'S':
    operacao2 = int(input('Deseja ver mais quantos termos? '))
    for i in range (0, operacao2):
        termo2 = termo2 + razao2
        print(f'{termo2}', end=' - ')
        quantidade2 += 1
    print(f'PAUSA')
    print()
    continua2 = input('Deseja ver mais termos? [S/N]: ').upper()
print(f'Operação finalizada com {quantidade2} termos mostrados.')
print('FIM')