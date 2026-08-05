import math

angulo_grau = float(input('Digite o valor de um ângulo: '))

angulo_radiano = math.radians(angulo_grau)

seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

print(f'Angulo informado: {angulo_grau:.0f}º')
print(f'Seno = {seno:.2f}')
print(f'Cosseno = {cosseno:.2f}')
print(f'Tangente = {tangente:.2f}')