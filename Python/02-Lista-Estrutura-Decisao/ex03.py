import os
os.system('cls')

sexo = str(input('Informe seu sexo: ').upper())

if sexo[0] == 'M':
    print('M - Masculino')
elif sexo[0] == 'F':
    print('F - Feminino')
else:
    print('Sexo Inválido')