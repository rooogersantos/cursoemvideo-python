print('Qual a escala da temperatura?')
escala = input('Digite "C" para Celsius(ºC) ou "F" para Fahrenheit(ºF): ').upper()

while escala != 'C' and escala != 'F':
   print('Parâmetros inválidos.')
   escala = input('Digite "C" para Celsius(ºC) ou "F" para Fahrenheit(ºF): ')

if escala == 'C':
   temp = float(input('Digite o valor da temperatura em ºC: '))
   temp_f = (temp * 1.8) + 32
   print(f'Temperatura convertida: {temp_f:.1f}ºF')
else:
   temp = float(input('Digite o valor da temperatura em ºF: '))
   temp_c = (temp - 32) * (5/9)
   print(f'Temperatura convertida: {temp_c:.1f}ºC')