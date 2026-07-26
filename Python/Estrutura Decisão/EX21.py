import os
os.system('cls')

saque = int(input("Informe valor de saque ( entre 10 e 600): "))

if saque < 10 or saque > 600:
      print("Valor inválido! Insira valor entre 10 e 600.")
else:
      nota_100 = saque // 100 # Pega o resultado da divisao ( número inteiro )
      saque = saque % 100 # O que sobrou do calculo anterior

      nota_50 = saque // 50
      saque = saque % 50
      
      nota_10 = saque // 10
      saque = saque % 10
      
      nota_5 = saque // 5
      saque = saque % 5
            
      nota_1 = saque // 1
      saque = saque % 1
      
      if nota_100 > 0:
            print(f"Nota 100 reais: {nota_100}")
      if nota_50 > 0:
            print(f"Nota 50 reais: {nota_50}")
      if nota_10 > 0:
            print(f"Nota 10 reais: {nota_10}")
      if nota_5 > 0:
            print(f"Nota 5 reais: {nota_5}")
      if nota_1 > 0:
            print(f"Nota 1 reais: {nota_1}")