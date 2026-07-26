import os
os.system('cls')


# <= Alcool 20L - desconto 3% por L
# > Alcool 20L - desconto 5% por L

# <= Gasolina 20L - desconto 4% por L
# > Gasolina 20L - desconto 6% por L

valor_L_gasolina = 2.50
valor_L_alcool = 1.90

# desconto_gasolina = 0.05
# desconto_alcool = 0.03

litros_vendidos = float(input("Litros vendidos: "))

tipo_combustivel = input("Tipo combustivel A-álcool, G-gasolina: ").lower()


if tipo_combustivel in "álcool alcool a":
    if litros_vendidos <= 20:
        desconto_alcool = 0.97
    elif litros_vendidos > 20:
        desconto_alcool = 0.95
        
    valor = litros_vendidos * valor_L_alcool
    
    valor_total = valor * desconto_alcool
    
    print(f"Valor total: R$ {valor_total:.2f}")

if tipo_combustivel in "gasolina g":
    if litros_vendidos <= 20:
        desconto_gasolina = 0.96
    elif litros_vendidos > 20:
        desconto_gasolina = 0.94
        
    valor = litros_vendidos * valor_L_gasolina
    
    valor_total = valor * desconto_gasolina
    
    print(f"Valor total: R$ {valor_total:.2f}")

