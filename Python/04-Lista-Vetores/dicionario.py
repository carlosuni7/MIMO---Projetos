import os
os.system('cls')

# AULA: DICIONARIO

# CRIANDO DICIONARIO ( "chave": valor)
personagem = {
    "nome": "Goku",
    "raca": "Sayajin",
    "transformacao" : "Super Sayajin",
    "poder": "kamehameha"
}

# print(personagem) # {'nome': 'Goku', 'raca': 'Sayajin', 'transformacao': 'Super Sayajin', 'poder': 'kamehameha'}

#ACESSANDO POR POSIÇÃO
print(personagem["nome"]) # -- Goku
print(personagem["poder"]) # -- Kamehameha

# DICIONARIO COM MAIS ELEMENTOS
personagem = [
    {
        "nome": "Goku",
        "raca": "Sayajin",
        "transformacao": "Instinto Superior",
        "poder": "kamehameha",
        "ki": 100
    },
    {
        "nome": "Vegeta",
        "raca": "Sayajin",
        "transformacao": "Super Ego",
        "poder": "Gallick Gun",
        "ki": 98
    },
]

# print(personagem) # ACESSA TODOS OS ELEMENTOS DO DICIONARIO

# ACESSANDO A POSICAO DO ELEMENTO E CHAVE
#print(personagem[1]["nome"]) # -- Vegeta
#print(personagem[1]["transformacao"]) # -- Super Ego
#print(personagem[0]["nome"])
#print(personagem[0]["transformacao"]) # -- Instito Superior : Goku

# CRIANDO DICIONARIO COM DICT( chave = valor)
pessoa = dict(
    nome = "Gohan",
    raca = "Humano-Sayajin",
    transformacao = "Mystic",
    poder = "Kamehameha",
    ki = 95
)
# ACESSANDO DICIONARIO
print(pessoa)
# ACESSANDO CHAVE DICIONARIO
print(pessoa["nome"]) # -- Gohan

# ALTERANDO VALAOR DA CHAVE
pessoa['nome'] = "Mistic Gohan";
print(pessoa)

# REMOVENDO CHAVE DO DICIONARIO
del pessoa['ki']
del pessoa['transformacao']
print(pessoa)

# ATUALIZANDO A CHAVE DO DICIONARIO - ADICIONAR CHAVE
pessoa.update({"roupa": "Laranja-Azul"})
print(pessoa)

# PEGAR VALOR COM MÉTODO GET()
print(pessoa.get('roupa'))

# REMOVER VALOR COM MÉTODO POP()
pessoa.pop('roupa')
print(pessoa)

# ADICIONANDO VARIOS VALORES NOVOS
pessoa.update({'transformacao':'Mystica Gohan', 'ki':95})
print(pessoa)

# REMOVER O ULTIMO ITEM DO DICIONARIO
pessoa.popitem()
print(pessoa)

# LIMPAR DICIONARIO
pessoa.clear()
print(pessoa)

carros = {
    'GM': 'Camaro',
    'lamborghini': 'Aventador ',
    'Ferrari': 'Enzo'
}
# PEGA AS KEYS DO DICIONARIO
print(carros.keys())
# PEGA OS VALORES DO DICIONARIO
print(carros.values())
# PEGA AS ( KEYS, VALORES) DO DICIONARIO CRIA UM ARRAY => TUPLA => KEY, VALOR
print(carros.items()) 

# PERCORRE AS KEYS DO DICIONARIO E EXIBE CADA VALOR
for chave in carros.keys():
    print(f'Chaves: {chave}')
    
# PERCORRE OS VALORES DO DICIONARIO E EXIBE CADA VALOR
for value in carros.values():
    print(f'Valores: {value}')
    
# PERCORRE CADA ITEM-VALOR DO DICIONARIO E EXIBE CADA VALOR
for item in carros.items():
    print(f'Item: {item}')
    

for chv, vlr in carros.items():
    print(f'ITEM:\n Chave: {chv} - Valor: {vlr}')
    
# Lista
nomes = ['Abner', 'Carlos', 'Otavio', 'Arthur']
idades = [25,23,22,12]

mini = {} # dicionario vazio
print('=='*20)
# COM zip - voce pode incluir varias lista
for nome, idade in zip(nomes, idades):
    print(f'{nome}: {idade}')
    mini[nome] = idade
    
# for nom, idad in zip(nomes, idades):
#     mini.update({'nome': nom, 'idade': idad})

print('=='*20)
print(mini)