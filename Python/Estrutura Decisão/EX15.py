import os
os.system('cls')

"""
comentario em varias linhas
"""
l1 = int(input("Primeiro lado triangulo: "))
l2 = int(input("Segundo lado triangulo: "))
l3 = int(input("Terceiro lado triangulo: "))


if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print(10*"=")
    print("É um triangulo:")
    
    if l1 == l2 == l3:
        print("Equilátero")
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("Isósceles")
    # com else, ele evita o trabalho atoa, pois ja passou da primeiras verificações entao, só pode ser escaleno
    else:
        print("Escaleno")
else: 
    print("Não pode ser um triangulo")
