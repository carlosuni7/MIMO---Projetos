import os
os.system('cls')

n1 = float(input("Insira primeira nota: "))
n2 = float(input("Insira segunda nota: "))
n3 = float(input("Insira terceira nota: "))
n4 = float(input("Insira quarta nota: "))

QtdNota = [n1,n2,n3,n4]


media = (n1 + n2 + n3 + n4) / len(QtdNota)

if media == 10:
    print('Aprovado com Distinção {}'.format(media))
elif media >= 7:
    print('Aprovado {}'.format(media))
elif media < 7:
    print('Reprovado {}'.format(media))