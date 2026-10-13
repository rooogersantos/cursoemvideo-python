# Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('=' * 40)
print('Informe abaixo quatro número inteiros')
print('-' * 70)

lista02 = (int(input('Digite o 1º número: ')),
            int(input('Digite o 2º número: ')),
            int(input('Digite o 3º número: ')),
            int(input('Digite o 4º número: ')))
print('-' * 70)
print(f'Você digitou os números: {lista02}')
print('-' * 70)

if lista02.count(9) == 0:
    print(f'O número "9" não foi digitado.')
elif lista02.count(9) == 1:
    print(f'O número "9" foi digitado {lista02.count(9)} vez.')
else:
    print(f'O número "9" foi digitado {lista02.count(9)} vezes.')
print('-' * 70)

if lista02.count(3) == 0:
    print(f'O número "3" não foi digitado.')
elif lista02.count(3) == 1:
    print(f'O número "3" apareceu na {lista02.index(3) + 1}ª posição.')
else:
    print(f'O número "3" apareceu mais de uma vez, sendo a primeira vez na {lista02.index(3) + 1}ª posição.')
print('-' * 70)

print('O(s) valor(es) par(es) digitado(s) foi/foram: ', end='')
for n in lista02:
    if n % 2 == 0:
        print(n, end=' ',)
print('\n' + '=' * 70)