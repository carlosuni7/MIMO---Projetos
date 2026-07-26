import os
os.system('cls')

ganhoHora = float(input("Quanto você ganha por hora: "))
horaMes = float(input("Quantas horas trabalha por mês: "))

def calcularSalario(valor, horas):
    salario = float(valor) * float(horas)
    return salario

print(f"Seu salario este mês foi: {calcularSalario(ganhoHora, horaMes):.2f} ")


