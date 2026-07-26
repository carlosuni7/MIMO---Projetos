import os
os.system('cls')

message = print('Informe o Turno que você estuda!')

turno = str(input('M - Matutino | V - Vespertino | N - Noturno: ')).lower()

if turno == 'm' or turno == 'matutino':
    print('Bom Dia!')
elif turno == 'v' or turno == 'vespertino':
    print('Boa Tarde!')
elif turno == 'n' or turno == 'noturno':
    print('Boa Noite!')
else:
    print('Valor Inválido!')