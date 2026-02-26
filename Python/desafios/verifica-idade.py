listaDePessoas = []

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
        "status": statusfun(idadeinput),
        "universo": "Dragon Ball Z"
    }
    return pessoa

# addPessoa = criar_pessoa(nome, idade)
# listaDePessoas.append(addPessoa)
# print(listaDePessoas)

i = True
while i:
    nome = input("Insira um nome: ")
    idade = int(input("Insira sua idade: "))

    #Funções devem ser independentes e reutilizáveis.
    addPessoa = criar_pessoa(nome, idade)

    listaDePessoas.append(addPessoa)
    print(listaDePessoas)

    pergunta =  input("Deseja continuar o Cadastro? ( S - Sim / N - Não)")
    resposta = pergunta.upper()
    
    if resposta == "S":
        continue
    else:
        break

print("\nLista Final de Pessoas: ")
for x in listaDePessoas:
    print(x)