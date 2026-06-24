import os
os.system('cls')


tamanho_arquivo = int(input("Informe o tamanho do arquivo (MB): "))
mbps = float(input("Informe a velocidade do links (Mbps): "))
print()

velocidade = mbps / 8

print(f"Tamanho do arquivo: {tamanho_arquivo}MB")
print(f"Internet: {mbps} Mbps")
print(f"Velocidade internet: {velocidade:.1f} MB/s")

segund_mb = tamanho_arquivo / velocidade
minutos = segund_mb/60

print(f"Minutos para dowload: {minutos:.1f}min")