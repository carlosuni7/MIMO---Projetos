import os
os.system('cls')

num = (input("Insira um numero: "))

texto_centena = ""
texto_dezena = ""
texto_unidade = ""

c = 0
d = 0
u = 0

if int(num) > 0 and int(num) < 1000:
    if len(num) == 3:
        c = int(num[0])
        d = int(num[1])
        u = int(num[2])
        
    elif len(num) == 2:
        d = int(num[0])
        u = int(num[1])
            
    elif len(num) == 1:
        u = int(num[0])
    
    if c > 1:
        texto_centena = "centenas"
    elif c == 1:
        texto_centena = "centena"
        
    if d > 1:
        texto_dezena = "dezenas"
    elif d == 1:
        texto_dezena = "dezena"
        
    if u > 1:
        texto_unidade = "unidades"
    elif u == 1:
        texto_unidade = "unidade"
    
    if c == 0:
        print(f'{d} {texto_dezena} e {u} {texto_unidade}')
    elif d == 0:
        print(f'{c} {texto_centena} e {u} {texto_unidade}')
    elif u == 0:
        print(f'{c} {texto_centena} e {d} {texto_dezena}') 
    else:
        print(f'{c} {texto_centena}, {d} {texto_dezena} e {u} {texto_unidade}') 
else:
    print("Insira válido e menor que 1000!")
    
# RETORNAR A ESTE EXERCICIO