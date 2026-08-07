soma = 0
cont = 0

for i in range(1, 500, 2):
    if i % 3 == 0 and i % 2 == 1:
        soma += i
        cont += 1
print(f'A soma de todos os números ímpares divisíveis por 3 entre 1 e 500 é {soma}.')
print(f'Há {cont} números com essas características entre 1 e 500.')