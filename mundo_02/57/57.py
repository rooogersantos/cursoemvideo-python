sexo = input('Informe o seu sexo [F/M]: ').upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    sexo = input('Opção inválida! Informe novamente o seu sexo [F/M]: ').upper().strip()[0]
if sexo == 'F':
    print(f'Sexo feminino registrado com sucesso!')
else:
    print(f'Sexo masculino registrado com sucesso!')