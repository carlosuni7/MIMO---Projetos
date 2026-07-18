import os
os.system('cls')

def impostoRenda(salario):
    if salario < 900:
        imposto_renda = 0
        return imposto_renda
    elif salario < 1500:
        imposto_renda = (5/100)
        return imposto_renda
    elif salario < 2500:
        imposto_renda = (10/100)
        return imposto_renda
    elif salario > 2500:
        imposto_renda = (20/100)
        return imposto_renda
    else:
        print('Insira um valor válido')
    
pergunta = input('Informe seu Salário Bruto: ')

salario_bruto = int(pergunta)

imposto_renda = impostoRenda(salario_bruto)
fgts = (11/100)
print(fgts)

print(f'Desconto do Imposto de Renda: {imposto_renda}%')



# print(f'Salário Bruto      :            R$ ')
# print(f'(-) IR (5%)        :            R$ ')
# print(f'(-) INSS ( 10%)    :            R$ ')
# print(f'FGTS (11%)         :            R$ ')
# print(f'Total de descontos :            R$ ')
# print(f'Salário Liquido    :            R$ ')