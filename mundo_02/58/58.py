import random
import time
tentativas = 0

numero_randomico = random.randint(0, 10)
chute = int(input('Pensei num número... Adivinhe! Digite um número de 0 a 10: '))
print()
print('Processando...')
print()
time.sleep(1)
tentativas = tentativas + 1

while chute > 10 or chute < 0:
    chute = int(input('Valor inválido! Digite novamente um número de 0 a 10: '))
    print()
    print('Processando...')
    print()
    time.sleep(1)

while chute != numero_randomico:
    if chute > numero_randomico:
        print('Que pena! Você não acertou a tentativa! É um número menor')
    elif chute < numero_randomico:
        print('Que pena! Você não acertou a tentativa! É um número maior')
    chute = int(input('Digite novamente um número de 0 a 10: '))
    print()
    print('Processando...')
    print()
    time.sleep(1)
    tentativas = tentativas + 1
    if chute > 10 or chute < 0:
        chute = int(input('Valor inválido! Digite novamente um número de 0 a 10: '))
        print()
        print('Processando...')
        print()
        time.sleep(1)

else:
    print('Parabéns! Você acertou a tentativa!')

print(f'Número sorteado = {numero_randomico}')
if tentativas == 1:
    print(f'Você acertou após {tentativas} tentativa.')
else:
    print(f'Você acertou após {tentativas} tentativas.')