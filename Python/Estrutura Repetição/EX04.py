import os
os.system('cls')

pop_A = 80000
pop_B = 200000
# Taxa anual de crescimento População A
taxa_anualA = (3 / 100)
# Taxa anual de crescimento População B
taxa_anualB = (1.5 / 100)

anos = 2026
count = 0
processando = True

while processando:
    count += 1
    anos += 1
    
    # Formas de atribuição a variavel
    crescimento_anual_A = int(pop_A * taxa_anualA)
    pop_A += crescimento_anual_A
    
    crescimento_anual_B = int(pop_B * taxa_anualB)
    pop_B = pop_B + crescimento_anual_B

    if pop_A >= pop_B:
        print("Objetivo alcançado!")
        print(f"Anos necessários: {count} anos")
        print(f"População A: {pop_A}")
        print(f"população B: {pop_B}")
        print(f"Ano atual: {anos}")
        processando = False