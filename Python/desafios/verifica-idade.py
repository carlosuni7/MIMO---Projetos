listaDePessoas = []
pessoa = {}

nome = input("Insira um nome: ")
idade = int(input("Insira sua idade: "))

#Funções devem ser independentes e reutilizáveis.
def statusfun(idade):
            if idade >= 18:
                return "Maior de idade"
            else:
                return "Menor de idade"
                
status = statusfun(idade)
    
def criar_pessoa(nome, idade, status):
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['status'] = status
    pessoa['universo'] = "Dragon Ball Z"
    return pessoa
    
addPessoa = criar_pessoa(nome, idade, status)

listaDePessoas.append(addPessoa)

print(listaDePessoas)