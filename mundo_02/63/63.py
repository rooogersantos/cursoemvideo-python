print('-'*65)
print('Sequência de Fibonacci')
print('-'*65)
n_elementos = int(input('Digite quantos números da sequência de Fibonacci você quer ver: '))
print('-'*65)
primeiro_termo = 0
segundo_termo = 1

if n_elementos == 0:
    print('Nenhum termo solicitado.')
elif n_elementos == 1:
    print(F'{primeiro_termo} - FIM')
else:
    print(f'{primeiro_termo} - {segundo_termo} - ', end='')

    for a in range (2, n_elementos):
        terceiro_termo = primeiro_termo + segundo_termo
        print(f'{terceiro_termo} - ', end='')
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
    print('FIM')
print('-'*65)