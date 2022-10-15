idade = input('Qual a sua idade? ')
sexo = input('Qual o seu sexo?("M" para Masculino e "F" para Feminino)')

if sexo.upper() == 'M':
    # Código para o Sexo Masculino
    if int(idade) >=65:
        print('Parabéns! Sua aposentadoria foi concedida')
    else:
        print(f'Aguarde mais {65 - int(idade)} anos para ser beneficiado')

elif sexo.upper() == 'F':
    # Código para o Sexo Feminino
    if int(idade) >=60:
        print('Parabéns! Sua aposentadoria foi concedida')
    else:
        print(f'Aguarde mais {60 - int(idade)} anos para ser beneficiado')

else:
    print('Opção inválida! Favor tentar novamente')
