import os
os.system('cls')

def calcularReajuste(sal, perce):
    reajuste = sal * (perce/100)
    novoSalario = sal + reajuste
    
    print(f'Valor sálario: R${sal}')
    print(f'Aumento de {perce}%')
    print(f'Valor do reajuste R$: {reajuste:.2f}')
    print(f'Novo sálario após aumento R$ {novoSalario:.2f}')


message = input('Informe seu Sálario: ')
salario = int(message)


if salario <= 280:
    # Porcentagem de aumento 20%
    resultado = calcularReajuste(salario, 20)
    print(resultado)
elif salario <= 700:
    # Porcentagem de aumento 15%
    resultado = calcularReajuste(salario, 15)
    print(resultado)
elif salario <= 1500:
    #  Porcentagem de aumento 10%
    resultado = calcularReajuste(salario, 10)
    print(resultado)
elif salario > 1500:
    # Porcentagem de aumento 5%
    resultado = calcularReajuste(salario, 5)
    print(resultado)
else:
    print('Insira um valor válido')
    
    