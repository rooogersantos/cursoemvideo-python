# Crie um programa onde o usuário possa digitar cinco
# valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista04 = []
print('=' * 65)

for i in range(0, 5):
    num04 = int(input('Digite um número: '))

    if i == 0 or num04 > lista04[-1]:
        lista04.append(num04)
        print('Adicionado ao final da lista!')
        print('-' * 65)
    else:
        pos = 0
        while pos < len(lista04):
            if num04 <= lista04[pos]:
                  lista04.insert(pos, num04)
                  print(f'Adicionado na {pos+1}ª posição da lista!')
                  print('-' * 65)
                  break
            pos += 1

print('Processo encerrado!')
print('=' * 65)
print(f'Os valores digitados em ordem crescente são: {lista04}')
print('=' * 65)