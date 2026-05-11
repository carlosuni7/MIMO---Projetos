import os
os.system('cls')

# numero = 2
# i = 0
# while i <= 10:
#     print('{} x {} = {}' .format(numero, i, (numero * i)))
#     i += 1
    
# --------------------------------

num = int(input('Digite um número pra ver sua tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))