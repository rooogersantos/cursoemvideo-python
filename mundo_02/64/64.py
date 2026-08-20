print('=' * 50)
numero = int(input('Digite um número inteiro entre 0 e 998: '))
entradas = soma = 0
print('-' * 50)

if numero >= 1000 or numero <= 0:
    print(f'Valor inválido.')
    numero = int(input('Digite um número inteiro entre 0 e 998: '))
    print('-' * 50)
else:
    while numero != 999:
        numero = int(input('Digite um número inteiro: '))
        print('-' * 50)
        while numero >= 1000 or numero <= 0:
            print(f'Valor inválido.')
            numero = int(input('Digite um número inteiro entre 0 e 998: '))
            print('-' * 50)
        soma = soma + numero
        entradas = entradas + 1

print(f'Processo encerrado.')

if entradas == 1:
    print(f'Foi digitado {entradas} número.')
    print(f'A soma é {soma}.')
elif entradas == 0:
    print(f'Não foi digitado nenhum número.')
else:
    print(f'Foram digitados {entradas} números.')
    print(f'A soma desses números é {soma}.')
print('=' * 50)