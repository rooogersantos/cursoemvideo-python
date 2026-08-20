import random
import time
tentativas = 0

while True:

    numero_programa = random.randint(0, 10)
    print('=' * 45)
    numero_meu = int(input('Digite um número: '))
    print('-' * 45)
    jogada = input('Par ou Ímpar [P/I]: ').upper()
    while jogada != 'P' and jogada != 'I':
        print('!' * 45)
        print('Opção inválida!')
        print('!' * 45)
        jogada = input('Par ou Ímpar [P/I]: ').upper().strip()
    print('-' * 45)
    total = numero_programa + numero_meu
    print('Processando...')
    print('-' * 45)
    time.sleep(1)
    print(f'Você jogou {numero_meu} e o programa jogou {numero_programa}, total {total}.')

    if total % 2 == 0:
        if jogada == 'P':
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    else:
        if jogada == 'I':
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    tentativas = tentativas + 1
print('-' * 45)
print('Jogo encerrado')
if tentativas == 0:
    print(f'Você não acertou nenhuma vez.')
elif tentativas == 1:
    print(f'Você acertou apenas {tentativas} vez.')
else:
    print(f'Você acertou {tentativas} vezes.')
print('=' * 45)