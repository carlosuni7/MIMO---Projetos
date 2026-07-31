import os
os.system('cls')

while True:
    
    nota = float(input("Insira uma nota entre zero e dez: "))
    
    if(nota >= 0 and nota <= 10):
        print("A nota é válida!")
        break
    
    else:
        print("Nota inválida!")
        print(10*"=")