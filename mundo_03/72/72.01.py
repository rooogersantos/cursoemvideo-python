# 072. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. 

tupla_01 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))
while numero > 20 or numero < 0:
    print('Número inválido!')
    numero = int(input('Digite novamente um número entre 0 e 20: '))
print(f'O número digitado é: {tupla_01[numero]}')