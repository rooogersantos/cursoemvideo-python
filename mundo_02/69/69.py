maiores = homens = mulheres_jovens = 0

while True:
    print('=' * 50)
    print('CADASTRO DE PESSOAS')
    print('-' * 50)
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    print('-' * 50)
    while continuar not in 'SN':
        print('Opção inválida!')
        sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_jovens += 1
    continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            print('Opção inválida!')
            continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break

print('=' * 50)
print('Processo de cadastramento encerrado!')
print('-' * 50)

if maiores == 0:
    print(f'Não foram cadastradas pessoas com mais de 18 anos.')
elif maiores == 1:
    print(f'Foi cadastrada {maiores} pessoa com mais de 18 anos.')
else:
    print(f'Foram cadastradas {maiores} pessoas com mais de 18 anos.')

if homens == 0:
    print(f'Não foi cadastrado nenhum homem.')
elif homens == 1:
    print(f'Foi cadastrado {homens} homem.')
else:
    print(f'Foram cadastrados {homens} homens.')

if mulheres_jovens == 0:
    print(f'Não foi cadastrada nenhuma mulher com menos de 20 anos.')
elif mulheres_jovens == 1:
    print(f'Foi cadastrada {mulheres_jovens} mulher com menos de 20 anos.')
else:
    print(f'Foram cadastradas {mulheres_jovens} mulheres com menos de 20 anos.')
print('=' * 50)