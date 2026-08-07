primeiro = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao

for n in range (primeiro, decimo + razao, razao):
  print(f'{n}', end=' - ')
print(f'FIM')