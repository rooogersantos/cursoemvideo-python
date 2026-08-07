print('-=' * 33)
print('Analisador de triângulos')
print('-=' * 33)

med1 = float(input('Digite o valor de uma das medidas: '))
med2 = float(input('Digite o valor de outra medida: '))
med3 = float(input('Digite o valor da última medida: '))

print('-=' * 33)
if med2 < (med1 + med3) and med1 < (med2 + med3) and med3 < (med1 + med2):
  print('Com essas medidas é possível formar um triângulo.')
  print('-=' * 33)

  if med1 == med2 == med3 == med1:
    print('Esse é um triângulo EQUILÁTERO.')
  elif med1 != med2 != med3 != med1:
    print('Esse é um triângulo ESCALENO.')
  else:
    print('esse é um triângulo ISÓCELES.')
  print('-=' * 33)

else:
  print('Com essas medidas não é possível formar um triângulo.')
  print('-=' * 33)