import os
os.system('cls')



# def cadastrarUsuario():
#     nome = input("Insira seu nome de usuario: ")
#     senha = input("Insira uma senha: ")

while True:
    nome = input("Insira seu nome de usuario: ")
    senha = input("Insira uma senha: ")
    
    if senha in nome:
        print("Erro ao inserir senha, tente novamente ")
        print("Insira uma nova senha diferente do nome de usuario ")
        print("---------------------------")
    else:
        print("Cadastrado com sucesso")
        break

