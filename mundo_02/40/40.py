nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print()

nota_final = (nota1 + nota2)/2

if nota_final < 5.0:
   print(f'Média final: {nota_final}. REPROVADO!')
elif nota_final < 6.9:
   print(f'Média final: {nota_final}. RECUPERAÇÃO!')
else:
   print(f'Média final: {nota_final}. APROVADO!')