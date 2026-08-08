lista_nomes = []
lista_idades = []
lista_generos = []

print('=' * 55)
print('Informe seus dados:')

for i in range(0,4):
    nome2 = input('Nome: ')
    lista_nomes.append(nome2)
    idade2 = int(input('Idade: '))
    lista_idades.append(idade2)
    sexo2 = input('Sexo("F"/"M"): ').upper()
    lista_generos.append(sexo2)
    print('-' * 55)

soma_idades2 = 0
for i in range(0,4):
    soma_idades2 = soma_idades2 + lista_idades[i]
idade_media2 = soma_idades2 / 4

homem_mais_velho = ''
maior_idade2 = 0
for i in range(0,4):
    if lista_generos[i] == 'M':
        if lista_idades[i] > maior_idade2:
            maior_idade2 = lista_idades[i]
            homem_mais_velho = lista_nomes[i]

mulheres_menos20 = 0
for i in range(0,4):
    if lista_generos[i] == 'F':
       if lista_idades[i] < 20:
          mulheres_menos20 += 1

print(f'A média das idades informadas é de {idade_media2:.2f} anos.')
print(f'O homem mais velho do grupo é {homem_mais_velho}, com {maior_idade2} anos.')
print(f'Há {mulheres_menos20} melheres com menos de 20 anos nesse grupo.')
print('=' * 55)