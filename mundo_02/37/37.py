numero_decimal2 = int(input('Digite um número inteiro qualquer: '))
print()

print('''Você quer converter esse número para que base numérica?
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - para Hexadecimal''')
base2 = input('Digite sua opção: ')
print()

while base2 not in ['1', '2', '3']:
   print('Opção inválida!')
   print('''Você quer converter esse número para que base numérica?
   [ 1 ] - Binário
   [ 2 ] - Octal
   [ 3 ] - Hexadecimal''')
   base2 = input('Digite sua opção: ')
   print()

if base2 == '1':
   print(f'Base escolhida: BINÁRIO.')
   print(f'O número {numero_decimal2} convertido para BINÁRIO é: {bin(numero_decimal2)[2:]}')
elif base2 == '2':
   print(f'Base escolhida: OCTAL.')
   print(f'O número {numero_decimal2} convertido para OCTAL é: {oct(numero_decimal2)[2:]}')
else:
   print(f'Base escolhida: HEXADECIMAL.')
   print(f'O número {numero_decimal2} convertido para HEXADECIMAL é: {hex(numero_decimal2)[2:].upper()}')