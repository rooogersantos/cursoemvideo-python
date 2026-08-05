dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

aluguel = (dias * 60) + (km * 0.15)

print(f'Valor a pagar: R${aluguel:.2f}')