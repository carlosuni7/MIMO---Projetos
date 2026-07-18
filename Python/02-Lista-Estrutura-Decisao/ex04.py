import os
os.system('cls')


letra = input('Digite uma letra: ').lower()
vogais = 'a e i o u '

if letra.isalpha():
    if letra in vogais:
        print('A letra "{}"'.format(letra), 'é uma vogal')
    else:
        print('A letra "{}"'.format(letra),'é um consoante')
else:
    print('Insira uma letra do alfabeto')
