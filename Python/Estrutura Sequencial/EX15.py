import os
os.system('cls')

# Porcentagens de descontos do salario
ds_IR = 0.11
ds_INSS = 0.08
ds_Sindicato = 0.05

# Inputs para entrada de valores
valor_hora = float(input("Quanto ganha por hora (R$): "))
horas_trabalho = int(input("Quantas horas trabalha por mês: "))

# Calculando salario 
salario_bruto = valor_hora * horas_trabalho
#  Calculando valor dos descontos
valor_IR = ds_IR * salario_bruto
valor_INSS = ds_INSS * salario_bruto
valor_Sindicato = ds_Sindicato * salario_bruto
#  Calculando valor salario liquido
salario_liquido = salario_bruto - valor_IR - valor_INSS - valor_Sindicato
print("//")
print("//")
print("====== Holerite ======")
print(f"+ Sálario bruto   : R$ {salario_bruto:.2f}")
print(f"- IR (11%)        : R$ {valor_IR:.2f}")
print(f"- INSS (8%)       : R$ {valor_INSS:.2f}")
print(f"- Sindicato (5%)  : R$ {valor_Sindicato:.2f}")
print(f"= Sálario Liquido : R$ {salario_liquido:.2f}")
