import os
os.system('cls')


nota1 = float(input("Insira 1° Nota: "))
nota2 = float(input("Insira 2° Nota: "))

# if 0 <= nota1 > 10 or 0 <= nota2 > 10:
#     print("Insira um nota de 0 a 10!")

conceito = None
status = None
media = ( nota1 + nota2 ) / 2

if 0 <= nota1 >= 10 and 0 <= nota2 >= 10:
    if media >= 9.0: # and media <= 10.0 ):
        conceito = "A"
        status = "APROVADO"
        
    elif media >= 7.5: # and media <= 9.0 ):
        conceito = "B"
        status = "APROVADO"
        
    elif media >= 6.0:# and media <= 7.5 ):
        conceito = "C"
        status = "APROVADO"
        
    elif media >= 4.0:# and media <= 6.0 ):
        conceito = "D"
        status = "REPROVADO"
        
    elif media >= 0:# and media <= 4.0 ):
        conceito = "E"
        status = "REPROVADO"
    else:
        conceito = ""
        status = ""
        media = "Nota inválida!"
    
    
    print(f'1° Nota: {nota1}')
    print(f'2° Nota: {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: {conceito}')
    print(f'Status: {status}')

else:
    print("Erro: Insira um nota de 0 a 10!")