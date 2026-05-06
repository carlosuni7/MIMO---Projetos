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
    
# processando = True

# while processando:
    
#     estadoCivil = input("Insira Estado Civil - S / C / V / D: ").upper()
    
#     if estadoCivil not in civilArr:
#         print("Opção inválida! Tente novamente.")
#         continue # Volta para o início do loop, sem executar o restante do código abaixo
    
#     if estadoCivil == 'S':
#             print('S - Solteiro(a)')
#     elif estadoCivil == 'C':
#         print('C - Casado(a)')
#     elif estadoCivil == 'V':
#         print('V - Viúvo(a)')
#     elif estadoCivil == 'D':
#         print('D - Divorciado(a)')
    
#     print(" Inseriu informação correta!")
#     processando = False # Encerra o loop

# Mapeamento de Estado Civil usando dicionário
# Chave: Letra digitada || Valor: Descrição complete

estados_civis = {
    'S': 'Solteiro(a)',
    'C': 'Casado(a)',
    'V': 'Viúvo(a)',
    'D': 'Divorciado(a)'
}

while True:
    esCivil = input("Insira Estado Civil - (S/C/V/D): ").upper()
    
    if esCivil in estados_civis:
        print(f"{esCivil} - {estados_civis[esCivil]}")
        print("✅ Informação processada com sucesso!")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")
        
# elif sexo[0] == 'F':
#     print('F - Feminino')
# else:
#     print('Sexo Inválido')


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

