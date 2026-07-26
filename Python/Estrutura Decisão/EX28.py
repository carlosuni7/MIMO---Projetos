import os
os.system('cls')

desconto_tabajara = 0.05

input("Carnes na Promoção: ( 1 - File Duplo ) ( 2 - Alcatra ) ( 3 - Picanha ): ")

tipo_carne = input("Informe tipo da carne: ").lower()
qtd = float(input("Quantidade: "))
tipo_pagamento = input("Tipo de Pagamento ( 1 - Dinheiro ) ( 2 - Pix ) ( 3 - Cartao Tabajara ): ")


if tipo_carne == "file duplo":
    if qtd > 5:
        preco_carne = 5.8
    else:
        preco_carne = 4.9
elif tipo_carne == "alcatra":
    if qtd > 5:
        preco_carne = 6.8
    else:
        preco_carne = 5.9
elif tipo_carne == "picanha":
    if qtd > 5:
        preco_carne = 7.8
    else:
        preco_carne = 6.9
    
valor_compra = preco_carne * qtd

if tipo_pagamento == "cartao tabajara" or tipo_pagamento == "3":
    valor_desconto = valor_compra * desconto_tabajara
    
    valor_total = valor_compra - valor_desconto
else:
    valor_total = valor_compra
    valor_desconto = 00.00
    

print("-"*16)
print(f"Tipo carne: {tipo_carne}")
print(f"Quantidade: {qtd:.3f}kg")
print(f"Preço carne: R$ {preco_carne:.2f}")
print("-"*10)
print(f"tipo de pagamento: {tipo_pagamento}")
print("-"*10)
print(f"Preço total: R$ {valor_compra:.2f}")
print(f"valor desconto: R$ {valor_desconto:.2f}")
print(f"Valor a pagar: R$ {valor_total:.2f}")









