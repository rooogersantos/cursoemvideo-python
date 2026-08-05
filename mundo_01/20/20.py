import random
alunos4 = []

for i in range(5):
    grupo = input(f'Digite o número de cada grupo: ').upper()
    alunos4.append(grupo)

random.shuffle(alunos4)
print(f'A ordem de apresentação dos grupos ficou assim:{alunos4}!')