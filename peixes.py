# Ler o peso de peixes trazidos por João
peso = float(input("Digite o peso de peixes trazidos por João (em quilos): "))

# Definir o limite estabelecido pelo regulamento
limite = 50  # Em quilos

# Verificar se o peso excede o limite
if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00  # R$ 4,00 por quilo excedente
else:
    excesso = 0
    multa = 0

# Exibir os resultados
print(f"João trouxe um peso de {peso} quilos de peixes.")
if excesso > 0:
    print(f"O peso excedeu o limite em {excesso:.2f} quilos.")
    print(f"João deverá pagar uma multa de R${multa:.2f}.")
else:
    print("João não precisa pagar nenhuma multa, pois o peso está dentro do limite estabelecido.")
