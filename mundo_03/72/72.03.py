# 072. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# CÓDIGO APRIMORADO

tupla_02 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    print('=' * 34)
    numero = int(input('Digite um número entre 0 e 20: '))
    print('-' * 34)
    while numero > 20 or numero < 0:
          print('Número inválido! Tente Novamente')
          numero = int(input('Digite um número entre 0 e 20: '))
          print('-' * 34)
    print(f'O número digitado é: {tupla_02[numero]}')
    print('-' * 34)
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    while continuar not in 'SN':
        print('Respostas inválida!')
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break

print('Processo encerrado')
print('=' * 34)