import os
os.system('cls')

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = ( nota1 + nota2 + nota3 ) / 3

if media == 10:
    print(f'Aprovado com distinção, nota: {media}!')
elif media >= 7:
    print(f'Aprovado, nota: {media}!')
else:
    print(f'Reprovado, nota: {media}!') 