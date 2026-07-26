import os
os.system('cls')
import math

pi:float = 3.14

raio:float = float(input("Insira um Raio de um Circulo: "))

def calcularArea(pi, raio):
    return pi * (raio * raio)

area:float = calcularArea(pi, raio)

print(f"A área do circulo é: {area:.1f}cm**2 ")

#Usando biblioteca Math

raio = float(input("Digite o raio: "))
area = math.pi * (raio ** 2)

print(f"A área do circulo é: {area:.2f}cm")