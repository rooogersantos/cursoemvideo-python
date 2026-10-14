# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
print('=' * 65)

while True:
    lista.append(int(input('Digite um número: ')))

    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    while continuar not in 'SN':
        print('Comando inválido')
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 65)
for n in range(0, len(lista)):
    if lista[n] % 2 == 1:
        lista_impar.append(lista[n])
    else:
        lista_par.append(lista[n])

print(f'A lista completa é {lista}')
print(f'A lista de números pares é {lista_par}')
print(f'A lista de números impares é {lista_impar}')
print('=' * 65)