data = input("Informe a data no formato dd/mm/aaaa: ")


dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

anoBisexto = False
if(ano % 4 == 0):
    anoBisexto = True
    
Valido = True
if (mes in (1,3,5,7,8,10,12)):
    if (dia < 1) or (dia > 31):
        Valido = False
elif (mes in (4,6,9,11)):
    if (dia < 1) or (dia > 30):
        Valido = False
elif mes == 2:
    if(anoBisexto):
        if(dia < 1) or (dia > 29):
            Valido = False
    else:
        if(dia < 1) or (dia < 28):
            Valido = False
else:
    Valido = False
    
if(Valido):
    print("Data Valida!")
else:
    print("Data invalida!")