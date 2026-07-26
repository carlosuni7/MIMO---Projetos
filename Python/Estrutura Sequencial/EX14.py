import os
os.system('cls')

# Controlar rendimento diario trabalho
# Trabalho com pesca de peixes
# Kg de peixes

# Peso estabelecido pelo regulamento de pesca do estado de São Paulo
peso_regulamento = 50.0
valor_multa_kilo = 4.00

peso_peixes = 0
excesso_peso_peixes = 0
#  calcular excesso de peso de peixe
#  calcular valor da multa pelo excesso

peso_peixes = float(input("Insira o peso de peixes: "))

if(peso_peixes > peso_regulamento):
    # Calculando peso excedente
    excesso_peso_peixes = peso_peixes - peso_regulamento
    # Calculando valor multa conforme peso excedente
    valor_multa = excesso_peso_peixes * valor_multa_kilo
    
    print(f'Total de excesso: {excesso_peso_peixes:.2f}kg')
    print(f'Total valor da multa: R${valor_multa:.2f}')
    

print(f'Total kilos de peixes: {peso_peixes:.2f}kg')