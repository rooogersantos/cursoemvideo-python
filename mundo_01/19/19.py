import random
alunos = []

for i in range(4):
   nome = input(f"Digite o {i+1}º nome da lista: ").upper()
   alunos.append(nome)

escolhido = random.choice(alunos)

print(f'O(A) escolhido(a) para apagar o quadro é: {escolhido}!')