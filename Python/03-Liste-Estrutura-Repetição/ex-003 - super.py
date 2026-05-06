import os
os.system('cls')

# def cadastrarUsuario():
#     nome = input("Insira seu nome de usuario: ")
#     senha = input("Insira uma senha: ")

# n = len(numeros)

# nome = input("Insira um Nome: ")
# idade = int(input("Insira um Idade: "))
# salario = float(input("Insira um Salário: "))
# sexo = input("Insira um sexo F - Feminino / M - Masculino").upper()

# estadoCivil = input("Insira Estado Civil - S / C / V / D: ").upper()
civilArr = ['S','C','V','D']


# if estadoCivil in civilArr:
#     print("Inseriu informação correta")
# else:
#     print("Insira uma opção correta!")
    
# i = True

# while i:
    
#     estadoCivil = input("Insira Estado Civil - S / C / V / D: ").upper()
    
#     if estadoCivil in civilArr:
#         print("Inseriu informação correta")
#         break
#     else:
#         print("Insira uma opção correta!")
#         continue
        
# ===============================
#  LOGICA VERIFICA ESTADO CIVIL
    
estados_civis = {
    'S': 'Solteiro(a)',
    'C': 'Casado(a)',
    'V': 'Viuvo(a)',
    'D': 'Divorciado'
}

processando = False
while processando:
    entrada = input("Insira Estado Civil - (S/C/V/D): ").upper()
    
    
    if entrada in estados_civis:
        print(f"{entrada} - {estados_civis[entrada]}")
        print(" ✅ Informação processada com Sucesso!")
        break
    else:
        print(" ❌ Informação inserida invalida")
        
    
idv_sexo = {
    'M': 'Masculino',
    'F': 'Feminino'
}

def verificaSexo():
    entrada_sexo = input("Insira seu sexo (M - Masculino / F - Feminino): ").upper()
    if entrada_sexo in idv_sexo:
        print(f"{entrada_sexo} - {idv_sexo[entrada_sexo]}")
    else:
        print("❌ Informação inserida invalida")

# verificaSexo()

def verificaNome():
    entrada_nome = input("Informe seu nome: ")
    x = 3 # Variavel aux. pra quantidade de caracteres
    if len(entrada_nome) < x:
        print(f"Insira nome maior que {x} caracteres")
    else:
        print(f"Olá, seja bem-vindo {entrada_nome}")


def verificaIdade():
    entrada_idade = input("Insira sua Idade")
    if entrada_idade > 0 and entrada_idade < 150:
        print(f"Você tem {entrada_idade} anos")
    else:
        print("❌ Idade inserida invalida")

    
# while True:
#     nome = input("Insira seu nome de usuario: ")
#     senha = input("Insira uma senha: ")
    
#     if senha in nome:
#         print("Erro ao inserir senha, tente novamente ")
#         print("Insira uma nova senha diferente do nome de usuario ")
#         print("---------------------------")
#     else:
#         print("Cadastrado com sucesso")
#         break

