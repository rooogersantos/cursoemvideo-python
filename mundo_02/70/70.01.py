print('=' * 50)
print('LOJA SUPER BARATÃO')
print('-' * 50)
total = preco = mais_caros =  mais_barato = 0

while True:
    produto = input('Informe o nome do produto: ').lower().strip()
    preco = float(input('Informe o preço: R$'))
    total += preco
    print('-' * 50)

    if preco > 1000:
        mais_caros += 1

    if mais_barato == 0:
        mais_barato = preco
    elif mais_barato > 0:
        if mais_barato > preco:
            produto_mais_barato = produto

    continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break

print('=' * 50)
print(f'O total da compra foi R${total:.2f}.')
if mais_caros == 0:
    print(f'Não temos produtos custando mais de R$1000.00.')
elif mais_caros == 1:
    print(f'Temos {mais_caros} produto custando mais de R$1000.00.')
else:
    print(f'Temos {mais_caros} produtos custando mais de R$1000.00.')
print(f'O produto mais barato: {produto_mais_barato}')
print('=' * 50)
print('Processo encerrado!')
print('=' * 50)