import os, math
os.system('cls')

# Classificação de inocencia
media = 0

#  Perguntas
pt1 = input("Telefonou para a vítima? (Sim - Não): ").lower()
pt2 = input("Esteve no local do crime? (Sim - Não): ").lower()
pt3 = input("Mora perto da vítima? (Sim - Não): ").lower()
pt4 = input("Devia para a vítima? (Sim - Não): ").lower()
pt5 = input("Já trabalho com a vítima (Sim - Não): ").lower()

if pt1 == "sim":
    media += 1
if pt2 == "sim":
    media += 1 
if pt3 == "sim":
    media += 1 
if pt4 == "sim":
    media += 1 
if pt5 == "sim":
    media += 1

if media > 5:
    print("Assasino")
elif media > 3:
    print("Cúmplice")
elif media == 2:
    print("Suspeita")
else:
    print("Inocente")