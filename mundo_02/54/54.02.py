from datetime import date
ano_atual2 = date.today().year
maiores2, menores2 = 0, 0

for i in range(1,8):
    ano_nascimento2 = int(input(f'Em que ano nasceu a {i}ª pessoa? '))
    if ano_atual2 - ano_nascimento2 >= 18:
        maiores2 += 1
    else:
        menores2 += 1
        
print()
print(f'Há {maiores2} pessoas maiores de idade nesse grupo:')
print(f'Há {menores2} pessoas menores de idade nesse grupo:')