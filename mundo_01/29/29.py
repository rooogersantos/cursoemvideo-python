velocidade = float(input('Velocidade lida: '))
print()

if velocidade > 80:
  valor_ultrapassado = velocidade - 80
  multa = valor_ultrapassado * 7.00
  print(f'Velocidade: {velocidade:.2f}km/h.')
  print('VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE PERMITIDA DE 80KM/H! FOI MULTADO!!')
  print(f'Valor da multa: R${multa:.2f}.')
else:
  print(f'Velocidade: {velocidade:.2f}km/h.')
  print(f'Velocidade dentro do valor permitido! Continue dirigindo com segurança!')