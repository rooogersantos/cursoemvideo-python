from datetime import date

ano2 = int(input('Digite um ano ou digite 0 para analizar o ano atual: '))
print()

if ano2 == 0:
   ano2 = date.today().year

if ano2 % 4 == 0 and ano2 % 100 != 00 or ano2 % 400 == 00 :
   print(f'O ano de {ano2} é um ano bissexto!')
else:
   print(f'O ano de {ano2} não é um ano bissexto!')