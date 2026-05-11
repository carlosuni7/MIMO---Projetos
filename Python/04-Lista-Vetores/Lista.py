import os
os.system('cls')

lista = [1,2,7.5,12,15, "Apple", "Samsung"]
print(lista)

# print(type(lista))

# print(lista[6])
# # Função para adicionar um elemento a variavel do tipo 'list'
# lista.append("carlos")
# # Pega o indice de tras pra frente e substitui o valor deste indice
#lista[-7] = "Abobora"
#lista[2] = "Celular"

# print(lista)

# # Ele pega os valores da lista apartir dos indice indica
# # Começa a lista a apartir do indice indicado - fatia a lista
print(lista[2:])
print(lista[2:5:])
print(lista[1:3:2])

# Pega a lista e exibe do ultimo para o primeiro elemento (inverte)
print(lista[::-1]) 
# print(lista)

# frutas = ["Banana", "Morango"]
# frutas.append("Maça")

# for fruta in frutas:
#     print(fruta)
# print("="*60)

# frutas.remove("Banana")
# for fruta in frutas:
#     print(fruta)
# print("="*60)

# frutas.append("Laranja")
# frutas.append("Limao")
# frutas.append("Abacate")
# frutas.append("Pera")
# frutas.append("Banana")
# # frutas.append("Abacate Limao Pera")
# for fruta in frutas:
#     print(fruta)
# print("="*60)

# # Sort() ordena a sua lista, retornando a mesma lista porem comm elemento ordenados
# # sort() ordena a lista original, uma vez feita não muda
# # Para evitar problemas o correto é criar uma cópia e então ordenar
# frutas.sort()
# for fruta in frutas:
#     print(fruta)
# print("="*60)

# # 
# # Para evitar problemas o correto é criar uma cópia e então reverter a lista
# frutas.reverse()
# for fruta in frutas:
#     print(fruta)
# print("/"*60)

# # Com enumerate eu consigo ter acesso ao indice e ao valor do elemento da lista
# for ind, vlr in enumerate(frutas):
#     print(f'{ind} - {vlr}')
#     print("-"*10)
#     print(f'{ind+1}')
# print("/"*60)

# fruta = frutas
# print(fruta)
# print(frutas)
# fruta.remove("Maça")    
# print("="*60)
# print(fruta)
# print(frutas)
# print("="*60)
# x = frutas.copy()
# print(x)
# print(type(x))
# x.remove("Laranja")
# print(x)

# Lista é mutavel - Ela pode mudar
# Tupla NÃO é mutavel - Ela permanece da forma que é criada no inicio

# lista = [1,2,3,4,5]
# tupla = (1,2,3,4,5)
# # lista[2] = 6
# print(lista)
# print(tupla)
# print("-"*40)

# lista.append(6)
# lista.insert()

# del lista
# lista.remove()

# # tupla[2] = 'Carlos' # tupla é imutavel não existe método append

# print(lista)
# print(len(tupla)) # Imprime a quantidade de itens da tupla
# print("-"*40)