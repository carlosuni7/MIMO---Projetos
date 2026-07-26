import os
os.system('cls')

n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
opcao = 0

while opcao != 5:
      print('-=-=-=-=-=-=--=-=-=-=')
      print('''               [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa''')
      opcao = int(input('Qual é sua opção: '))
      print('-=-=-=-=-=-=--=-=-=-=')
      match opcao:
            case 1:
                  soma = n1 + n2
                  print(f'A soma entre {n1} + {n2} = {soma}')
            case 2:
                  produto = n1 * n2
                  print(f'O resultado de {n1} x {n2} = {produto}')
            case 3:
                  if n1 > n2:
                        maior = n1
                  else:
                        maior = n2
                  print(f'O maior numero entre {n1} e {n2} é {maior}')
            case 4:
                  print('Informe os números novamente: ')
                  n1 = int(input('Primeiro valor: '))
                  n2 = int(input('Segundo valor: '))
            case 5:
                  print('Finalizando o programa...')
            case _:
                  print('Opção inválida. Tente novamente.')

# print('Fim do programa! Volte sempre!')






# n = int(input("Quantos termos de Fibonacci você quer gerar? "))
# ultimo = 1
# penultimo = 1

# if n >= 1:
#     print(ultimo)
# if n >= 2:
#     print(penultimo)

# i = 3
# while i <= n:
#     proximo = ultimo + penultimo
#     print(proximo)
#     penultimo = ultimo
#     ultimo = proximo
#     i = i + 1