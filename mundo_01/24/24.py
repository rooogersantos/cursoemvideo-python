nome_cidade = input('Digite o nome de uma cidade: ').strip().upper()
print()

if 'SANTO' in nome_cidade:
    print('A palavra "SANTO" faz parte do nome dessa cidade!')
else:
    print('Não há a palavra "SANTO" no nome dessa cidade!')