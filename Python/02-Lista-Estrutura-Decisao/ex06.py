n1 = int(input('Insira primeiro numero: '))
n2 = int(input('Insira segundo numero: '))
n3 = int(input('Insira terceiro numero: '))

maior = n1

if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3

print('O maior número é: {}'.format(maior))




