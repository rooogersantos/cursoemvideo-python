from datetime import date

ano_nascimento = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print()

if idade < 18:
  saldo = 18 - idade
  if saldo == 1:
    print(f'Você tem {idade} anos.\nAinda não está em idade de alistamento militar!\nFalta {saldo} ano!')
  else:
    print(f'Você tem {idade} anos.\nAinda não está em idade de alistamento militar!\nFaltam {saldo} anos!')
  print(f'Seu alistamento será em {ano_nascimento + 18}.')
elif idade == 18:
  print(f'Você tem {idade} anos.\nChegou o momento de realizar o alistamento militar!')
else:
  saldo = idade - 18
  if saldo == 1:
    print(f'Você tem {idade} anos. Já passou do período de alistamento Militar!\nVocê deveria ter se alistado há {saldo} ano.')
  else:
    print(f'Você tem {idade} anos. Já passou do período de alistamento Militar!\nVocê deveria ter se alistado há {saldo} anos.')
  print(f'Seu alistamento deveria ter sido em {ano_nascimento + 18}.\nVERIFIQUE SUA SITUAÇÃO!')