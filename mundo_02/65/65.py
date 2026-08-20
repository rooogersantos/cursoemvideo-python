numero03 = int(input('Digite um número inteiro: '))
soma03 = numero03
entradas03 = 1
maior03 = numero03
menor03 = numero03

continuar = input('Deseja digitar mais algum número? [S/N]? ').upper().strip()

while continuar != 'S' and continuar != 'N':
    print('Opção inválida!')
    continuar = input('Digite "S"(para continuar) ou "N"(para finalizar):').upper().strip()

while continuar == 'S':
    numero03 = int(input('Digite um número inteiro: '))
    soma03 = soma03 + numero03
    entradas03 = entradas03 + 1

    if maior03 < numero03:
        maior03 = numero03

    if menor03 > numero03:
        menor03 = numero03

    continuar = input('Deseja digitar mais algum número? [S/N]? ').upper().strip()

    while continuar != 'S' and continuar != 'N':
        print('Opção inválida!')
        continuar = input('Digite "S"(para continuar) ou "N"(para finalizar):').upper()

media03 = soma03 / entradas03
print(f'A média dos números digitados é {media03:.2f}.')
print(f'O maior número digitado é {maior03}.')
print(f'O menor número digitado é {menor03}.')