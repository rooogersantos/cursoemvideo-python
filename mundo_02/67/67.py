print('=' * 100)
print('Desafio da tabuada')
print('=' * 100)
a = int(input('Digite um número inteiro positivo para descobrir sua tabuada: '))
print('=' * 100)

while True:
    for i in range (1,11):
        print(f'{a} x {i} = {a*i}')
    print('=' * 100)
    a = int(input('Digite outro número para descobrir sua tabuada (Digite um número negativo para encerrar o processo): '))
    print('=' * 100)
    if a < 0:
        break
print('Processo encerrado!')
print('=' * 100)