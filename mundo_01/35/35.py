print('-=' * 27)
print('Analisador de triângulos')
print('-=' * 27)
print()

med1 = float(input('Digite o valor de uma medida: '))
med2 = float(input('Digite o valor de outra medida: '))
med3 = float(input('Digite o valor da última medida: '))
print()

print('-=' * 27)
if med2 < (med1 + med3) and med1 < (med2 + med3) and med3 < (med1 + med2):
  print('Com essas medidas é possível formar um triângulo.')
else:
  print('Com essas medidas não é possível formar um triângulo.')
print('-=' * 27)