# Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista01 = []

print('=' * 40)
print('Informe abaixo quatro número inteiros')
print('-' * 40)
for i in range (4):
    numero01 = int(input(f'Digite o {i + 1}º número inteiro: '))
    lista01.append(numero01)
tuple(lista01)
print('-' * 40)

if lista01.count(9) == 0:
    print(f'O número "9" não foi digitado.')
elif lista01.count(9) == 1:
    print(f'O número "9" foi digitado {lista01.count(9)} vez.')
else:
    print(f'O número "9" foi digitado {lista01.count(9)} vezes.')

if lista01.count(3) == 0:
    print(f'O número "3" não foi digitado.')
elif lista01.count(3) == 1:
    print(f'O número "3" apareceu uma vez na {lista01.index(3) + 1}ª posição.')
else:
    print(f'O número "3" apareceu mais de uma vez, sendo a primeira vez na {lista01.index(3) + 1}ª posição.')

listapares = []
for i in range (4):
    if lista01[i] % 2 == 0:
       listapares.append(lista01[i])

if len(listapares) == 0:
    print(f'Não foram digitados números pares.')
elif len(listapares) == 1:
    print(f'O números par digitado foi: {listapares}')
else:
    print(f'Os números pares digitados foram: {listapares}')

print('=' * 40)