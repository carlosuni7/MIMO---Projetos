import os
os.system('cls')

x = 3

match(x):
    case 1:
        print("Hoje é ", end='')
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Sabado")
    case _:
        print("Nenhum opção escolhida")