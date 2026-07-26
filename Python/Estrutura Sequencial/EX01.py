# end="" - Imprimi varias palavras na mesma linha

print("Hello World", end=" ")
print("Carlos Alessandro")

print("Eu tenho", 23, "anos")
print("=======")
"""
Aqui coloco
varias linhas
de comentário
"""
""""
x = str(3)
y = int(3)
z = float(3)

print(type(x), type(y), type(z))
"""
#Multiplos valores para multiplas variaveis
"""
x, y, z = "laranja", "mamao", "melancia"
print(x)
print(y)
print(z)
print("=========")
"""

# Desempacotar uma coleção
fruits = ["apple", "banana", "cherry"]
apple, banana, cherry = fruits
print(apple)
print(banana)
print(cherry)
print(apple + banana + cherry)
print("=========")

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Nesta função criei uma variavel local que só pode ser usada dentro da função
def segfunc():
    x = "fantastic"
    print("Python is " + x)

segfunc()
print("Python is " + x)

# Voce pode criar dentro da função a variavel como global e usa-la em qualquer lugar
def terfun():
    global x
    x = "super"

terfun()
print("Python is " + x)