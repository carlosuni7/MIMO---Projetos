import os
os.system("cls")

# se definir a atribuição da variavel dentro do loop
# # sempre será feito a atribuição a cada iteração

# Então dependendo da ordem que os valores forem inseridos
# a condicional nunca será aplicada

i = 1
maior = int(input(f"insira {i}° número: "))

while i < 5:
    i += 1
    num = int(input(f"insira {i}° número: "))

    if num > maior:
        maior = num  


    
print(f"Maior número: {maior}")    
         

