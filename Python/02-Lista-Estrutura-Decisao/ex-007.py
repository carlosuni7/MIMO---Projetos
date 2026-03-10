import os
os.system('cls')

n1 = int(input('Insira primeiro numero: '))
n2 = int(input('Insira segundo numero: '))
n3 = int(input('Insira terceiro numero: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3


print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))


# Testar de forma diferente
lista_numeros = []
numeros = [5, 20, 35, 11, 6, 9, 10, 55, 78, 0]

# Criando um laço for para repetir de acordo com a quantidade de numero dentro do array 'numeros'
for i in numeros:
    # num = int(input(f'Insira o {i+1}° número: '))
    num = i
    # Adiciona cada numero do array
    lista_numeros.append(num)

print(f'Maior: {max(lista_numeros)} | Menor: {min(lista_numeros)}')
