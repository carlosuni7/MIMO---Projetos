import math
import os
os.system('cls')

#  Loja de Tintas
#  Input - Tamanho em metros quadrados da area a ser pintada
#  1 Litro de tinta cobre 3 metros quadrados
#  Lata vendida possui 18 litros - custa R$ 80,00

# cobertura da tinta em metros
cobertura_tinta = 3
# valor latas de tinta (18L)
valor_latas = 80.00
litro_lata = 18

metro_area = int(input("Informe o metro quadrado da área: ")) # valor em metros quadrados*
qtd_litros = metro_area / cobertura_tinta # calculo do valor de litros de tinta

# math.ceil() (O teto) - arrendonda o valores de float pra cima/próximo número inteiro maior ex: 4.1 ou 4.9 vai pra 5
# math.floor() (O chão) - arredonda os valores de float pra baixo/proximo numero inteiro menor ex: 4.1 ou 4.9 vai pra 4
qtd_latas = math.ceil(qtd_litros / litro_lata) # calcular da quantidade de latas pelo total de litros
preco_total = qtd_latas * valor_latas # calculando o valor total das latas

print(f"Total de litros: {qtd_litros:.1f}L")
print(f"Quantidade de latas: {qtd_latas} unidades")
print(f"Preço total: R$ {preco_total:.2f}")