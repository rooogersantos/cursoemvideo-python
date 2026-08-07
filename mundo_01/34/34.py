salario_atual = float(input('Informe o salário do colaborador: '))
print()

if salario_atual > 2500:
   aumento = salario_atual * 0.10
   salario_aumento = salario_atual + aumento
else:
   aumento = salario_atual * 0.15
   salario_aumento = salario_atual + aumento

print(f'Valor do aumento: R${aumento:.2f}')
print(f'Valor do salário com aumento R${salario_aumento}.')