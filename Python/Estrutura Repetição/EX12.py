import os
os.system('cls')

# Gerador de tabuada

process = True
while process:
    continuar = True
    num = int(input("insira um número: "))
    
    # conforme ( regra de negócio ). o if faz validação que verifica
    # se o número estará entre 1 e 10
    if num <= 0 or num > 10:
        print("insira número entre 1 e 10!")
        continue
    
    print(f"Tabuada de {num}")
    for t in range(1,11):
        print(f"{num} x {t} = {num * t}")
        
    while continuar: 
        cont = input("Deseja inserir outro valor? (S/N): ").upper()
        if cont == "N":
            process = False
            break
        elif cont != "S":
            print("Opção inválida!")
            continue
        else:
            continuar = False