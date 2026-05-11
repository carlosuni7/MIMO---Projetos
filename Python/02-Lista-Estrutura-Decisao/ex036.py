casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos ele vai pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100


print('Pra pagar uma casa de R$ {:.2f} em {} anos' . format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}' .format(prestacao))