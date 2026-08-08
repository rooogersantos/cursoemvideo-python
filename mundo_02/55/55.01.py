pesos = []
nomes = []
maior_peso = 0
menor_peso = 0
nome_maior_peso = ''
nome_menor_peso = ''

print('=' * 40)
for i in range(0,5):
    nome1 = input('Digite seu nome: ')
    nomes.append(nome1)
    peso1 = float(input('Digite o seu peso: '))
    pesos.append(peso1)
    print('-' * 40)

for i in range(0,5):
    if pesos[i] > maior_peso:
        maior_peso = pesos[i]
        nome_maior_peso = nomes[i]

menor_peso = pesos[0]
for i in range(1,5):
    if pesos[i] < maior_peso:
        menor_peso = pesos[i]
        nome_menor_peso = nomes[i]

print(f'O maior peso informado: {nome_maior_peso}, {maior_peso:.3f}kg.')
print(f'O menor peso informado: {nome_menor_peso}, {menor_peso:.3f}kg.')
print('=' * 40)