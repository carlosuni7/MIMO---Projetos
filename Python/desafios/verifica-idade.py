listaDePessoas = []

nome = input("Insira um nome: ")
idade = int(input("Insira sua idade: "))

#Funções devem ser independentes e reutilizáveis.
def statusfun(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
                

def criar_pessoa(nomeinput, idadeinput):
    pessoa = {
        "nome": nomeinput,
        "idade": idadeinput,
        "status": statusfun(idade),
        "universo": "Dragon Ball Z"
    }
    return pessoa

addPessoa = criar_pessoa(nome, idade)
listaDePessoas.append(addPessoa)
print(listaDePessoas)

i = 1
while i < 2:
    
    nome = input("Insira um nome: ")
    idade = int(input("Insira sua idade: "))

    #Funções devem ser independentes e reutilizáveis.
    def statusfun(idade):
        if idade >= 18:
            return "Maior de idade"
        else:
            return "Menor de idade"
                

    def criar_pessoa(nomeinput, idadeinput):
        pessoa = {
        "nome": nomeinput,
        "idade": idadeinput,
        "status": statusfun(idade),
        "universo": "Dragon Ball Z"
        }
        return pessoa

    addPessoa = criar_pessoa(nome, idade)
    listaDePessoas.append(addPessoa)
    print(listaDePessoas)

