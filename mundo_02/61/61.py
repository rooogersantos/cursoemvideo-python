print(f'Vamos criar uma Progressão Aritmética com 10 termos.')
primeiro = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão da PA: '))
operacao = 1
termo = primeiro
print(f'{termo}', end=' - ')

while operacao < 10:
   termo = termo + razao
   print(f'{termo}', end=' - ')
   operacao += 1
print(f'FIM')