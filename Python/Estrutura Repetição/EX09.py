import os
os.system('cls')

print("Exibindo números impares entre 1 e 50")
for c in range(1,51):
    if c % 2 != 0:
            print(c)

# num = int(input('Digite um número pra ver sua tabuada: '))
# for c in range(1,11):
#     print('{} x {:2} = {}'.format(num, c, num * c))

# # :2 serve para reservar um espaço dentro da chave 
# # pra quando o format substituir o valor
# print('-' * 12)
# print('{} x {:2} = {}'.format(num, 1, num * 1))
# print('{} x {:2} = {}'.format(num, 2, num * 2))
# print('{} x {:2} = {}'.format(num, 3, num * 3))
# print('{} x {:2} = {}'.format(num, 4, num * 4))
# print('{} x {:2} = {}'.format(num, 5, num * 5))
# print('{} x {:2} = {}'.format(num, 6, num * 6))
# print('{} x {:2} = {}'.format(num, 7, num * 7))
# print('{} x {:2} = {}'.format(num, 8, num * 8))
# print('{} x {:2} = {}'.format(num, 9, num * 9))
# print('{} x {:2} = {}'.format(num, 10, num * 10))