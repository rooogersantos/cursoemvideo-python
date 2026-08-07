import random
from time import sleep

print('Bem vindo!\nVamos jogar JOKENPÔ?')

opcoes2 = ['', 'PEDRA', 'PAPEL', 'TESOURA']
numero_randomico2 = random.randint(1, 3)
chute2 = int(input('''Digite um número:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura\nChute: '''))
print()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print()

print(f'Sua escolha: {opcoes2[chute2]}')
print(f'Escolha do jogo: {opcoes2[numero_randomico2]}')
print()

if chute2 == numero_randomico2:
  print('Vish... Empatamos!')
elif (chute2 == 1 and numero_randomico2 == 3) or \
     (chute2 == 2 and numero_randomico2 == 1) or \
     (chute2 == 3 and numero_randomico2 == 2):
  print('Parabéns! Você venceu!!!')
else:
  print('Que pena... Você perdeu!!!')