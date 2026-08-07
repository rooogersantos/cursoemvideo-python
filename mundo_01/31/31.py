distancia_viagem = float(input('Digite a distância da viagem em km: '))
print()

if distancia_viagem < 200:
   valor_passagem = distancia_viagem * 0.50
   print(f'Valor da passagem = R${valor_passagem:.2f}')
else:
   valor_passagem = (200 * 0.50) + ((distancia_viagem - 100) * 0.45)
   print(f'Valor da passagem = R${valor_passagem:.2f}')