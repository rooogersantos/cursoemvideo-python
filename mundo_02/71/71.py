while True:

    print('=' * 50)
    print('BANCO CEV'.center(50))
    print('=' * 50)

    saque = float(input('Quanto você desejar sacar? R$'))
    while saque % 2 == 1:
        print('Valor inválido!')
        print('Saque disponível apenas para valores pares.')
        print('=' * 50)
        saque = float(input('Informe novamente o valor do saque: R$'))

    notas_50 = saque // 50
    notas_20 = (saque % 50) // 20
    notas_10 = (saque % 20) // 10
    notas_2 = (saque % 10) // 2
    break

print('=' * 50)
if notas_50 == 1:
    print(f'Total de {notas_50:.0f} cédula de R$50.00.')
if notas_50 > 1:
    print(f'Total de {notas_50:.0f} cédulas de R$50.00.')
if notas_20 == 1:
    print(f'Total de {notas_20:.0f} cédula de R$20.00.')
if notas_20 > 1:
    print(f'Total de {notas_20:.0f} cédulas de R$20.00.')
if notas_10 == 1:
    print(f'Total de {notas_10:.0f} cédula de R$10.00.')
if notas_10 > 1:
    print(f'Total de {notas_10:.0f} cédulas de R$10.00.')
if notas_2 == 1:
    print(f'Total de {notas_2:.0f} cédula de R$2.00.')
if notas_2 > 1:
    print(f'Total de {notas_2:.0f} cédulas de R$2.00.')
print('=' * 50)