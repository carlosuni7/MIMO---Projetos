import os
os.system('cls')

celsius = float(input("Insira uma temperatura em celsius: "))

farenheit = float( (celsius * (9/5)) + 32 )

resposta = input(f"A temperatura celsius em Farenheit: {farenheit:.1f}F°")