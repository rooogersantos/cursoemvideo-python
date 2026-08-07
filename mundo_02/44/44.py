valor_produto = float(input('Informe o valor do produto: R$'))
forma_pagamento = input('''Digite o número correspondente à forma de pagamento:

  1 - Dinheiro/cheque
  2 - A vista no cartão
  3 - Cartão 2x
  4 - Cartão 3x\n''')

while forma_pagamento not in ['1', '2', '3', '4']:
   print('Opção INVÁLIDA!')
   forma_pagamento = input('''Digite NOVAMENTE o número correspondente à forma de pagamento:

  1 - Dinheiro/cheque
  2 - A vista no cartão
  3 - Cartão 2x
  4 - Cartão 3x\n''')

if forma_pagamento == '1':
   print(f'Forma de pagamento: A vista com dinheiro/cheque.')
   print(f'Valor original: R${valor_produto:.2f}.')
   print(f'Valor do desconto: R${valor_produto * 0.10:.2f}')
   print(f'Valor final: R${(valor_produto) - valor_produto * 0.10:.2f}')
   
elif forma_pagamento == '2':
   print(f'Forma de pagamento: A vista no cartão.')
   print(f'Valor original: R${valor_produto:.2f}.')
   print(f'Valor do desconto: R${valor_produto * 0.05:.2f}')
   print(f'Valor final: R${(valor_produto) - valor_produto * 0.05:.2f}')

elif forma_pagamento == '3':
   print(f'Forma de pagamento: Parcelado no cartão 2x.')
   print(f'Valor final: R${valor_produto:.2f}')
   print(f'Valor da parcela: R${valor_produto/2:.2f}')

elif forma_pagamento == '4':
   parcela = int(input('Será parcelado em quantas vezes? '))
   valor_parcela = valor_produto/parcela
   print(f'Forma de pagamento: Parcelado no cartão {parcela}x.')
   print(f'Valor original: R${valor_produto:.2f}.')
   print(f'Valor do acréscimo(juros 20%): R${valor_produto * 0.20:.2f}')
   print(f'Valor final: R${(valor_produto) + valor_produto * 0.20:.2f}')
   print(f'Valor da parcela: R${valor_parcela:.2f}')