import os
os.system('cls')

vetor = []
y = 0

# Entrada de Valor
while len(vetor) < 4:

    nota = float(input(f'Informe {len(vetor)+1}° nota: '))
    if(nota < 0 or nota > 10):
        print('valor inválido!')
        continue
        
    vetor.append(nota)

# Processamento de valor
print('='*20)  
print('Notas: ',)
for n,x in enumerate(vetor):
    y += x
    print(f'{n+1}° = {x} ')
        
# Saida de Valores
print('='*20)  
print('Média:', end='')
media = y/len(vetor)
print(media)



    
# y = 0
# for v in vetor:
#     y += v
#     print(y)
    
    