import math
# math.ceil() (O teto) - arrendonda o valores de float pra cima/próximo número inteiro maior ex: 4.1 ou 4.9 vai pra 5
# math.floor() (O chão) - arredonda os valores de float pra baixo/proximo numero inteiro menor ex: 4.1 ou 4.9 vai pra 4
import os
os.system('cls')

#  Loja de Tintas
#  Input - Tamanho em metros quadrados da area a ser pintada
#  1 Litro de tinta cobre 6 metros quadrados
#  Lata vendida possui 18 litros - custa R$ 80,00

cobertura_tinta = 6
litro_lata = 18
litro_galao = 3.6
valor_lata = 80.00 # valor lata de tinta (18L)
valor_galao = 25.00 # valor galao de tinta (3,6L)


area = int(input("Informe o metro quadrado da área: ")) # valor em metros quadrados*
print()
#  exercicio pede pra adicionar um folga 10%. Num orçamento seria fazer com que sobrasse ou fazer com uma folga mesmo, pra nao acabar faltando material

qtd_litros = area / cobertura_tinta # calculo do valor de litros de tinta

qtd_latas = math.ceil(qtd_litros / litro_lata) # calcular da qtd de latas pelo total de litros
qtd_galoes = math.ceil(qtd_litros / litro_galao) # calcular da qtd de galões pelo total de litros

preco_total_latas = valor_lata * qtd_latas # calculando o valor total das latas
preco_total_galoes = valor_galao * qtd_galoes

# qtd_latas_mistura = math.ceil((qtd_litros/2) / litro_lata) # calcular da qtd de latas pelo total de litros
# qtd_galoes_mistura = math.ceil((qtd_litros/2) / litro_galao) # calcular da qtd de galões pelo total de litros

# preco_latas_mistura = valor_lata * qtd_latas_mistura # calculando o valor total das latas
# preco_galoes_mistura = valor_galao * qtd_galoes_mistura
# preco_total_mistura = preco_galoes_mistura + preco_latas_mistura

print(f"==== Orçamento para Latas de 18L ====")
print(f"Quantidade de latas: {qtd_latas} unidades")
print(f"Preço total: R$ {preco_total_latas:.2f}")
print()
print(f"==== Orçamento para Galões de 3.6L ====")
print(f"Quantidade de Galões: {qtd_galoes} unidades")
print(f"Preço total: R$ {preco_total_galoes:.2f}")
