frase1 = input('Digite uma frase: ').upper().replace(" ", "").strip()
frase2 = frase1[::-1]

if frase1 == frase2:
  print('É PALÍDROMO!')
else:
  print('NÃO É PALÍNDROMO!')