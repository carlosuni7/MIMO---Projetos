inMetro = 1.80
inCentimetro = 180

def converterParaMetro( centimetro ):
    return centimetro / 100

def converterParaCentimetro( metro ):
    return metro * 100

toCentimetro = converterParaCentimetro( inMetro )
toMetro = converterParaMetro(inCentimetro)


print(f"Eu Carlos tenho {toMetro}m de altura em metro")
print(f"Eu carlos tenho {toCentimetro:.0f}cm de altura em centimetro")


