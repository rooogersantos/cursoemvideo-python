print('Insira abaixo os dados solicitados: ')
valor_imovel = float(input('Valor do imóvel: R$'))
salario = float(input('Salário: R$'))
tempo = int(input('Tempo para o pagamento(anos): '))
prestacao = valor_imovel / (tempo * 12 )
print()

print(f'Simulação de empréstimo para compra de imóvel, valendo R${valor_imovel:.2f} para pagamento em {(tempo * 12)} meses - {tempo} anos.')
if prestacao > (salario * 0.33):
   print(f'O valor da prestação simulada é de R${prestacao:.2f} e excede 1/3 do salário (R${salario:.2f}). EMPRÉSTIMO NEGADO!')
else:
   print(f'O valor da prestação simulada é de R${prestacao:.2f} e não excede 1/3 do salário (R${salario:.2f}). EMPRÉSTIMO APROVADO!')