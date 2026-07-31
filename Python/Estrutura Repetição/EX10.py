import os
os.system("cls")

print("Exibindo intervalo entre dois números inteiros")

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

# swap - troca de variaveis
if b < a:
    d = a # variavel auxiliar pra troca
    a = b # trocando os valores de variaveis
    b = d
    # caso A ficasse com valor maior que B
    # daria erro no range, ex: 
    # range(5,1) : o range acaba nao realizando a função pois da erro 
    # estrutura range: range(inicio, termino, intervalo )
    # no termino do range(inicio, 'termino') : o termino não é contado, o range acabo no valor anterior

# print("A:",a)
# print("B:",b)

for c in range(a + 1,b):
    print(c)
