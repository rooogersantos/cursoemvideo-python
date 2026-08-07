soma = 0
cont = 0
for b in range(0, 6):
  numero = int(input('Digite um número inteiro: '))
  if numero % 2 ==0:
     soma += numero
     cont += 1
print(f'VOCÊ DIGITOU {cont} NÚMEROS PARES E A SOMA DESSES NÚMEROS É {soma}')