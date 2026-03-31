import os
os.system('cls')

farenheit = float(input("Insira uma temperatura em farenheit: "))

celsius = float( (5 * (farenheit - 32)) / 9 )

resposta = input(f"A temperatura farenheit em Celsius: {celsius:.1f}")