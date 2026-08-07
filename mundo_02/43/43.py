print('-=' * 20)
print('IDENTIFICADOR DE IMC')
print('-=' * 20)

peso = float(input('Digite o seu peso: '))
print('-=' * 20)
altura = float(input('Digite a sua altura: '))
print('-=' * 20)

imc = peso / (altura * altura)

if imc < 18.5:
   print(f'IMC = {imc:.2f}. ABAIXO DO PESO')
elif imc <= 25:
   print(f'IMC = {imc:.2f}. PESO IDEAL')
elif imc <= 30:
   print(f'IMC = {imc:.2f}. SOBREPESO')
elif imc <= 40:
   print(f'IMC = {imc:.2f}. OBESIDADE')
elif imc > 40:
   print(f'IMC = {imc:.2f}. OBESIDADE MÓRBIDA')
print('-=' * 20)
