maior_idade = 18
idade_especial = 12

idade = int(input('Informe sua idade: '))

if idade >= maior_idade:
    print('Maior de idade, pode tirar CHN')

if idade < maior_idade:
    print('Ainda não pode tirar a CNH')    

if idade >= maior_idade:
    print('Maior de idade, pode tirar a CNH.')
else:
    print('Ainda não pode tirar a CNH')    

