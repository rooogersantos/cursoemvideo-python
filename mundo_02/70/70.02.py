total02 = mais_caros02 = menor_preco02 = contador02 = 0
produto_mais_barato02 = ' '

print('=' * 50)
print('LOJA SUPER BARATÃO')
print('=' * 50)

while True:
    produto02 = input('Nome do produto: ')
    preco02 = float(input('Preço do produto: R$'))
    contador02 += 1
    total02 += preco02
    print('-' * 50)

    if preco02 > 1000:
        mais_caros02 += 1

    if contador02 == 1:
        menor_preco02 = preco02
        produto_mais_barato02 = produto02
    else:
        if preco02 < menor_preco02:
            menor_preco02 = preco02
            produto_mais_barato02 = produto02

    resp = ' '
    while resp not in 'SN':
        resp = input('Desejar continuar? [S/N]').strip().upper()[0]
        print('-' * 50)
    if resp == 'N':
        break

print(f'O total da compra foi R${total02:.2f}.')
if mais_caros02 == 0:
    print(f'Não temos produtos custando mais de R$1000.00.')
elif mais_caros02 == 1:
    print(f'Temos {mais_caros02} produto custando mais de R$1000.00.')
else:
    print(f'Temos {mais_caros02} produtos custando mais de R$1000.00.')
print(f'O produto mais barato: {produto_mais_barato02} (R${menor_preco02:.2f})')
print('=' * 50)
print('Processo encerrado!')
print('=' * 50)