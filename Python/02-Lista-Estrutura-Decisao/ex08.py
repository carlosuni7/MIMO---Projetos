import os
os.system('cls')

produto1 = float(input('Insira o valor 1° produto: '))
produto2 = float(input('Insira o valor 2° produto: '))
produto3 = float(input('Insira o valor 3° produto: '))


produtos = []
produtos = produto1, produto2, produto3


print(f'Escolha comprar o produto de valor: R$ {min(produtos)}')