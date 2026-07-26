import os
os.system('cls')

salario = int(input('Informe seu Sálario: '))
porcentagem = 0

if salario <= 280:
    # Porcentagem de aumento 20%
    porcentagem = 20
    reajuste = salario * (porcentagem/100)
    novoSalario = salario + reajuste

elif salario <= 700:
    # Porcentagem de aumento 15%
    porcentagem = 15
    reajuste = salario * (porcentagem/100)
    novoSalario = salario + reajuste
    
elif salario <= 1500:
    #  Porcentagem de aumento 10%
    porcentagem = 10
    reajuste = salario * (porcentagem/100)
    novoSalario = salario + reajuste
    
elif salario > 1500:
    # Porcentagem de aumento 5%
    porcentagem = 5
    reajuste = salario * (porcentagem/100)
    novoSalario = salario + reajuste
else:
    print('Insira um valor válido')
    
    
print(f'Valor sálario: R${salario}')
print(f'Aumento de {porcentagem}%')
print(f'Valor do reajuste R$: {reajuste:.2f}')
print(f'Novo sálario após aumento R$ {novoSalario:.2f}')