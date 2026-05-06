import os
os.system('cls')

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'M m F f':
    sexo = str(input('Dados inválidos. Por favor insira seu sexo [M/F]: ')).strip().upper()[0]
    
if sexo in 'M m':
    print('Sexo masculino registrado com sucesso!')
elif sexo in 'F f':
    print('Sexo feminino registrado com sucesso!')

