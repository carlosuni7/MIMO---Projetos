import os
os.system('cls')

sexo = str(input("Informe o sexo - ( M - masculino | F - feminino): ")).lower()

if(sexo in ("M m masculino")):
    altura = float(input("Informe sua altura: "))
    peso = (72.7 * altura) - 58
    print(f"Peso ideal para altura masculina {altura:.2f}m: {peso:.2f}kg")
    
elif(sexo in ("F f feminino")):
    altura = float(input("Informe sua altura: "))
    peso = (62.1 * altura) - 44.7
    print(f"Peso ideal para altura feminina {altura:.2f}m: {peso:.2f}kg")