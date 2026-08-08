from datetime import date
ano_atual = date.today().year

nomes_maiores, nomes_menores = [], []
idades_maiores, idades_menores = [], []
maiores, menores = 0, 0

for i in range (0,7):
    nome_pessoa = input('Digite seu nome: ')
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maiores += 1
        idades_maiores.append(idade)
        nomes_maiores.append(nome_pessoa)
    else:
        menores += 1
        idades_menores.append(idade)
        nomes_menores.append(nome_pessoa)

print()
print(f'Há {maiores} pessoas maiores de idade nesse grupo:')
for nome, idade in zip(nomes_maiores, idades_maiores):
    print(f'{nome}, {idade} anos')
print()

print(f'Há {menores} pessoas menores de idade nesse grupo:')
for nome, idade in zip(nomes_menores, idades_menores):
    print(f'{nome}, {idade} anos')