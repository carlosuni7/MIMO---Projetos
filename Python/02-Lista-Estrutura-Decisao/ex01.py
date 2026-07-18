import os
os.system('cls')

number1 = int(input('Insira primeiro número: '))
number2 = int(input('Insira segundo número: '))

if number1 > number2:
    print(f'O número {number1} é maior que {number2}')
else:
    print(f'O número {number2} é maior que {number1}')