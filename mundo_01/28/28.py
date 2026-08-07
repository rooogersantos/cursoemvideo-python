import random
import time

numero_randomico = random.randint(0, 5)
chute = int(input('Adivinhe o número! Digite um número de 0 a 5: '))
print()
print('Processando...')
print()
time.sleep(2)

if chute > 5 or chute < 0:
   chute = int(input('Valor inválido! Digite novamente um número de 0 a 5: '))
   print()
   print('Processando...')
   print()
   time.sleep(2)

if chute == numero_randomico:
   print('Parabéns! Você acertou a tentativa!')
else:
   print('Que pena! Você não acertou a tentativa!')

print(f'Número sorteado = {numero_randomico}')