from math import sqrt, pow

cat1 = float(input('Digite a medida de um dos catetos: '))
cat2 = float(input('Digite a medida do outro cateto: '))
hip = sqrt(pow(cat1, 2) + pow(cat2, 2))

print(f'A medida da hipotenusa é {hip:.2f}.')