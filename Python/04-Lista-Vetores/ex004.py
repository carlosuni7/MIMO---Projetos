import os
os.system('cls')

vetor = []
vogais = ['a','e','i','o','u']
x = 10
print('Insira 10 Caracteres: ')


while len(vetor) < x:
    char = str(input(f'Informe {len(vetor)+1}° caracter: '))
    vetor.append(char)
    
print(vetor)


# if vetor not in consoante:
#     print(vetor)