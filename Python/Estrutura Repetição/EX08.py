import os
os.system('cls')

# i = 0
# notas = 0
# process = True
# qtd_provas = 5

# while process:
#     i+=1
#     num = float(input(f"insira {i}° número: "))
#     notas += num
    
#     if i == qtd_provas:
#         media = notas / i
#         print(f"Média: {media}")
#         break
        
for c in range(1,6):
    num = float(input(f"insira {c}° número: "))
    notas += num

media = notas / 5
print(f"Média: {media}")