frase3 = input('Digite uma frase: ').upper().strip()
palavras = frase3.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]

if inverso == junto:
  print('Temos um PALÍNDROMO!')
else:
  print('A frase digitada NÃO É UM PALÍNDROMO!')