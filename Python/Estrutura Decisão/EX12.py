import os
os.system('cls')

des_IR = 0
sindicato = 0.03
inss = 0.1
fgts = 0.11
hora = int(input("Quantidade de horas trabalhadas: "))
vlr_hora = float(input("Valor das horas: "))

# Calcula o salario bruto, com os valores que o usuario inseriu
salario_bruto = hora * vlr_hora

# Fluxo de controle para definir o valor de desconto do Imposto de Renda
if salario_bruto <= 900:
    # desconto IR - isento
    des_IR = 0
    # vlr_IR = des_IR * salario_bruto
elif salario_bruto <= 1500:
    # desconto IR - 5%
    des_IR = 0.05
    vlr_IR = des_IR * salario_bruto
elif salario_bruto <= 2500:
     # desconto IR - 10%
    des_IR = 0.1
    # vlr_IR = des_IR * salario_bruto
elif salario_bruto > 2500:
     # desconto IR - 20%
    des_IR = 0.2
    # vlr_IR = des_IR * salario_bruto
else:
    print('Insira um valor válido')

# Calculo do valor em reais do desconto de IR
vlr_IR = des_IR * salario_bruto

# Valores em reais dos desconto
vlr_sindicato = sindicato
vlr_inss = inss * salario_bruto
vlr_fgts = fgts * salario_bruto # FGTS 11% do sálario bruto

total_desconto = (des_IR + inss) * salario_bruto
salario_liquido = salario_bruto - (vlr_IR + vlr_inss)


print("Salário Bruto: ({:.0f} * {})   :            R$ {:.2f}".format(vlr_hora,hora, salario_bruto))
print(f'(-) IR ({des_IR*100:.0f}%)                :            R$ {vlr_IR:.2f}'.format(des_IR*100))
print("(-) INSS ({:.0f}%)             :            R$ {:.2f}".format(inss*100, vlr_inss))
print(f'FGTS ({fgts*100:.2f}%)             :            R$ {vlr_fgts:.2f}')
print(f'Total de descontos           :            R$ {total_desconto:.2f}')
print(f'Salário Liquido              :            R$ {salario_liquido:.2f}')