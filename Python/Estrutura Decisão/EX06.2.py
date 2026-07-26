import os
os.system('cls')

numeros = [15, 8, -5, 42, -80, 99, 3, 27, 19, 50, 11, 6, 34, 2, 45, 18, 9, 31, 14, 7, 25, 40, 12]

#  Devo consolidar a ideia de estado de variavel
maior = numeros[0]
menor = numeros[0]

for num in numeros:
    #  aqui fiz comparação com a vairavel anterior ja encontrada como sendo o maior numero
    if num > maior:
        maior = num
    if num < menor:
        menor = num

# for num in numeros:
#     if num < menor:
#         menor = num
        
print("Maior numero: {}".format(maior))
print("Menor numero: {}".format(menor))