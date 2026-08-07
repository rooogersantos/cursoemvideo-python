from datetime import date

ano_nasc = int(input('Informe a idade do atleta: '))
ano = date.today().year
idade = ano - ano_nasc

print(f'O atleta tem {idade} anos.')
if idade <= 9:
   print(f'Categoria: MIRIM.')
elif idade <= 14:
   print(f'Categoria: INFANTIL.')
elif idade <= 19:
   print(f'Categoria: JÚNIOR.')
elif idade <= 25:
   print(f'Categoria: SÊNIOR.')
else:
   print(f'Categoria: MASTER.')