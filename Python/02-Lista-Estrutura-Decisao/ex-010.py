import os
os.system('cls')

message = print('Informe o Turno que você estuda!')

turno = input('M - Matutino | V - Vespertino | N - Noturno: ').lower()

if turno[0] == 'm' and turno == 'matutino':
    print('Bom Dia!')
elif turno[0] == 'V' and turno == 'vespertino':
    print('Boa Tarde!')
elif turno[0] == 'N' and turno == 'noturno':
    print('Boa Noite!')
else:
    print('Valor Inválido!')