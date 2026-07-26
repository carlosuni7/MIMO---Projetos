import os
os.system('cls')


valor = input("informe um ano: ")

# aqui adiciono os dois ultimos digitos do ano a uma variavel
ano = int(valor)
# Erro: a lógica quebra se o usuario inserir um ano : 99 ou 10000
# a fatia funciona quando o ano possui 4 digitos apenas
# final = int(valor[2:])

# # verifica se o ano termina em 00
# if final != 00:
#     if ano % 4 == 0:
#         print(f'O ano {ano}: Bissexto')
#     else:
#         print(f'O ano: {ano}: Não é bissexto')
# else:
#     # se o ano termina com 00
#     # verifica se e divisivel por 400 pra verifica se e bissexto ou nao
#     if ano % 400 == 0:
#         print(f'O ano {ano}: Bissexto')
#     else:
#         print(f'O ano: {ano}: Não é bissexto')
        
        
if ano % 400 == 0:
    print(f'O ano: {ano} é bissexto')
elif ano % 100 == 0:
    print(f'O ano: {ano} não é bissexto')
elif ano % 4 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano: {ano} não é bissexto')
        
