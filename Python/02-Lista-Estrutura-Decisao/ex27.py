totalMorangos = int(input("Informe a quantidade Kg de morango: "))
totalMaca = int(input("Informe a quantidade de Kg de maça: "))

if totalMorangos <= 5:
    valorMorango = totalMorangos * 2.5
else:
    valorMorango = totalMorangos * 2.2


if totalMaca <= 5:
    valorMaca = totalMaca * 1.8
else:
    valorMaca = totalMaca * 1.5
    
print("Valor de Morangos: ", valorMorango)
print("Valor de Maças: ", valorMaca)

valorBruto = valorMorango + valorMaca
valorLiquido = valorBruto
if (valorMaca+valorMorango > 8) or (valorBruto > 25):
    valorLiquido = valorBruto * 0.9
    
print("Valor bruto da compra: ", valorBruto)
print("Peso total da compra: ", (totalMaca+totalMorangos))
print("Valor Liquido da compra: ", valorLiquido)
            