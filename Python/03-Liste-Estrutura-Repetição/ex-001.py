import os
os.system('cls')

def pergunta():
    nota = float(input("Insira uma nota entre zero e dez: "))
    return nota

while True:
    numero = pergunta()
    
    if(numero >= 0 and numero <= 10):
        print("O valor inserido é valido!")
        break
    
    else:
        print("O valor inserido e INvalido")