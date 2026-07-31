import os
os.system('cls')

# A lógica permite que o usuario informe as populações e taxas de crescimento
# para as duas cidades e realize a comparação

process = True
calculando = True

print("Calculo de Crescimento populacional paralelo")
while process:
    # Reiniciando as variaveis auxiliares
    calculando = True
    # Toda vez que o while principal inicia torna o calculando True pra que sempre calcule quando passar das verificações
    anos = 2026
    count = 0
    continuar = True
    
    pop_A = int(input("Informe número população A: "))
    taxa_A = float(input("informe a taxa de crescimento A ( % ): "))
    
    pop_B = int(input("Informe número população B: "))
    taxa_B = float(input("informe a taxa de crescimento B ( % ): "))
    
    if pop_A < 0:
        print("Numero populacional A inválida")
        continue
    elif pop_A >= pop_B:
        print("População A já é maior que População B")
        continue
    elif taxa_A <= taxa_B:
        print("A taxa de crescimento de A deve ser maior que a de B para alcançá-la!")
        continue
    if pop_B < 0:
        print("Número populacional B inválida")
        continue
        
    taxa_anualA = taxa_A / 100
    taxa_anualB = taxa_B / 100
    
    while calculando:
        count += 1
        anos += 1
        
        # Formas de atribuição a variavel
        crescimento_anual_A = int(pop_A * taxa_anualA)
        pop_A += crescimento_anual_A
        
        crescimento_anual_B = int(pop_B * taxa_anualB)
        pop_B = pop_B + crescimento_anual_B
        
        if pop_A >= pop_B:
            calculando = False
    
    print(15*"-")
    print("Objetivo alcançado!")
    print(f"Anos necessários: {count} anos")
    print(f"População A: {pop_A}")
    print(f"Taxa crescimento A: {taxa_A:.1f}%")
    print(f"população B: {pop_B}")
    print(f"Taxa crescimento B: {taxa_B:.1f}%")
    print(f"Ano atual: {anos}")
    print(15*"-")

    #  Pequeno while pra validar se o usuarios deseja realizar 
    #  calculo de uma nova cidade
    while continuar: 
            cont = input("Deseja realizar um novo cálculo com outras cidades? (S/N): ").upper()
            if cont == "N":
                process = False
                break
            elif cont != "S":
                print("Opção inválida!")
                continue
            else:
                continuar = False