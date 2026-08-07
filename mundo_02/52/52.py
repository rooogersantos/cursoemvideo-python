num2 = int(input('Digite um número: '))
while num2 == 0 or num2 < 0:
    num2 = int(input('Número inválido. Digite outro número: '))

tot2 = 0

print()
for i in range(1, num2 + 1):
    if num2 % i == 0:
        print(f'O número {num2} é divisível por {i}')
        tot2 += 1

print()
if tot2 == 2:
    print(f'O número {num2} é divisível por apenas {tot2} números')
    print(f'Portanto, o número {num2} é um número primo.')
elif num2 == 1:
    print(f'O número {num2} é divisível apenas por ele mesmo')
    print(f'Portanto, o número {num2} não é um número primo.')
else:
    print(f'O número {num2} é divisível por {tot2} números')
    print(f'Portanto, o número {num2} não é um número primo.')