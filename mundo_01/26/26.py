frase4 = input('Escreva uma frase qualquer: ').upper().strip()
print()

if frase4.count('A') == 0:
  print(f'Não Foi encontrada qualquer letra "a" na frase digitada.')
elif frase4.count('A') == 1:
  print(f'Foi encontrada apenas {frase4.count('A')} letra "a" na frase digitada.')
else:
  print(f'Foram encontradas {frase4.count('A')} letras "a" na frase digitada.')

print(f'A primeira letra "A" apareceu na posição {frase4.find('A')+1} da frase.')
print(f'A última letra "A" apareceu na posição {frase4.rfind('A')+1} da frase.')