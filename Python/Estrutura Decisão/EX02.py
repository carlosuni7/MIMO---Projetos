import os
os.system('cls')

number = float(input('Insira um número: '))

if number > 0:
    print('Seu número é positivo!-')
elif number < 0:
    print('Seu número é negativo!')
else:
    print("Número é ZERO")