# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

num = []
pares = []
impares = []
print('=' * 65)

while True:
    num.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    while continuar not in 'SN':
        print('Comando inválido')
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 65)
for i, v in enumerate(num):
    if v % 2 == 1:
        impares.append(v)
    elif v % 2 == 0:
        pares.append(v)

print(f'A lista completa é {num}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números impares é {impares}')
print('=' * 65)