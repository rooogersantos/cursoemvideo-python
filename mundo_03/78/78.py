# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

lista = []

print('=' * 65)
for a in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {a+1}: ')))
    if a == 0:
        maior = menor = lista[a]
    else:
        if lista[a] <= menor:
            menor = lista[a]
        if lista[a] > maior:
            maior = lista[a]
print('-' * 65)

print(f'Você digitou os valores: {lista}')

print('-' * 65)

print(f'O menor valor digitado foi {menor}, na(s) posição(ões): ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print(f'\nO maior valor digitado foi {maior}, na(s)  posição(ões): ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print('')
print('=' * 65)