print('Digite três números:')
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))
print()

if num1 > num2 and num1 > num3:
  print(f'O primero número informado é o maior: {num1}.')
elif num2 > num1 and num2 > num3:
  print(f'O segundo número informado é o maior: {num2}.')
else:
  print(f'O terceiro número informado é o maior: {num3}.')

if num1 < num2 and num1 < num3:
  print(f'O primero número informado é o menor: {num1}.')
elif num2 < num1 and num2 < num3:
  print(f'O segundo número informado é o menor: {num2}.')
else:
  print(f'O terceiro número informado é o menor: {num3}.')