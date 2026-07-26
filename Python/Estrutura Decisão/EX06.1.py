import os
os.system('cls')

n1 = int(input('Insira 1° numero: '))
n2 = int(input('Insira 2° numero: '))
n3 = int(input('Insira 3° numero: '))

#  Uso uma variavel de estado para comparações futuras
maior = n1
#  aqui fiz comparação com a vairavel anterior ja encontrada como sendo o maior numero
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

#  Meu erro foi querer fazer comparação com cada variavel, ao invés de pensar no maior ja encontrado, por isso o algoritmo falha em algumas situação, 
# O legal foi armazenar um valor como maior
# O seguinte e fazer a comparação com a atual e a maior ja encontrada
#  e não so comparar entre os número em si

# if n2 > n1:
#     maior = n2
# if n3 > n2:
#     maior = n3

print('O maior número é: {}'.format(maior))




