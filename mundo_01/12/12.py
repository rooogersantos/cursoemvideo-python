preco = float(input('Digite o valor do produto: R$'))

preco_desc = preco - (preco * 0.05)

print()
print(f'O preço com desconto: R${preco_desc:.2f}')