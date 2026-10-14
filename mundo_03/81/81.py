# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista02 = []
print('=' * 65)

while True:
    lista02.append(int(input('Digite um número: ')))

    continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    while continuar not in 'SN':
        print('Comando inválido')
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    if continuar == 'N':
        break
print('-' * 65)
print(f'Foram digitados {len(lista02)} números.')

print('-' * 65)

print(f'Os valores em ordem decrescente são: ', end='')
lista02.sort(reverse=True)
print(lista02)
print('-' * 65)

if 5 not in lista02:
    print('O número 5 não foi encontrado nessa lista!')
else:
    print('O número 5 faz parte desta lista!')
print('=' * 65)