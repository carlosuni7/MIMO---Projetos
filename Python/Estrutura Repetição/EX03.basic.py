import os
os.system('cls')
# n = len(numeros)

processar = True
x = 3 # Qtd de caracter
while processar:
    nome = input("Insira um Nome: ")
    idade = int(input("Insira sua idade: "))
    salario = int(input("Informe seu sálario: "))
    sexo = input("Insira um sexo F - Feminino / M - Masculino: ").upper()
    estado_civil = input("Insira Estado Civil - S / C / V / D: ").upper()
    
    print(14*"-")
    if len(nome) < x:
        print(f"nome inválido(a)") 
    else:
        print(f"Olá {nome}")

    if idade < 0 or idade > 150:
        print("idade inválida!")
    else:
        print(f"Você tem {idade} anos")
        
    if salario < 0:
        print("salario inválido!")
    else:
        print(f"Sálario R$ {salario},00")
    if sexo != 'FEMININO' or sexo != 'MASCULINO':
        print("gênero inserido inválido(a)!")
    else:
        print(f"Sexo: {sexo}")
        
    if estado_civil not in "S C V D":
        print("estado civil inválido(a)!")
    else:
        print(estado_civil.upper())
    
    processar = False
else:
    processar = True