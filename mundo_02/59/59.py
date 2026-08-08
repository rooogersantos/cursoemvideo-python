print('Digite dois valores:')
valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
print()
operacao_solicitada = int(input('''Que operação você deseja realizar?

[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA: '''))
print()

while operacao_solicitada > 5 or operacao_solicitada < 1:
    print('Número inválido!')
    operacao_solicitada = int(input('''Digite novamente a operação você deseja realizar?

[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA: '''))
    print()

while operacao_solicitada != 5:

    if operacao_solicitada == 1:
        soma = valor1 + valor2
        print(f'{valor1} + {valor2} = {soma}.')
        print()

    elif operacao_solicitada == 2:
        multiplicacao = valor1 * valor2
        print(f'{valor1} x {valor2} = {multiplicacao}.')
        print()

    elif operacao_solicitada == 3:
        if valor1 > valor2:
            print(f'O primeiro número ({valor1}) é maior que o segundo número ({valor2}).')
        elif valor1 < valor2:
            print(f'O segundo número ({valor2}) é maior que o primeiro número ({valor1}).')
        else:
            print(f'O primeiro número ({valor1}) e o segundo número ({valor2}) são iguais.')
        print()

    elif operacao_solicitada == 4:

        print('Digite novamente dois valores:')
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
        print()

    elif operacao_solicitada > 5 or operacao_solicitada < 5:
        print('Número inválido!')
        operacao_solicitada = int(input('''Digite novamente a operação você deseja realizar

[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA: '''))
        print()

    operacao_solicitada = int(input('''Que operação você deseja realizar?

[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA: '''))
    print()
print('Finalizado!')