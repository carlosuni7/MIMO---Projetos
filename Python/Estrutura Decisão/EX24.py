import os, math
os.system('cls')

num1 = float(input("Insira primerio numero: "))
num2 = float(input("Insira segundo numero: "))
op = input("Escolha operação: + | - | * | / : ")


if op == "+":
    resultado = num1 + num2
if op == "-":
    resultado = num1 - num2
if op == "*":
    resultado = num1 * num2
if op == "/":
    resultado = num1 / num2
    
arr = round(resultado)
# Verifica se o numero e inteiro ou decimal
if resultado == arr:
    print("Numero inteiro!")
else:
    print("Numero decimal")
    
#  verifica se o numero e par ou impar
if resultado % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")
    
#  verifica se o numero e positivo ou negativo
if resultado >= 0:
    print("Numero positivo")
elif resultado < 0:
    print("Numero negativo")
    
print(resultado)