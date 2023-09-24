Função para calcular o preço de custo
def calcular_preco_custo(valor_produto, quantidade, imposto1, imposto2, imposto3, valor_frete):
    preco_custo = valor_produto * quantidade + imposto1 + imposto2 + imposto3 + valor_frete
    return preco_custo

# Função para calcular o preço de venda
def calcular_preco_venda(preco_custo):
    preco_venda = preco_custo * 1.6  # Adiciona 60% ao preço de custo
    return preco_venda

# Solicitar entrada de dados do usuário
valor_produto = float(input("100"))
quantidade = int(input("100"))
imposto1 = float(input("60"))
imposto2 = float(input("150"))
imposto3 = float(input("100 "))
valor_frete = float(input("50"))

# Calcular o preço de custo
preco_custo = calcular_preco_custo(100, 100, 60, 150, 100, 50)

# Calcular o preço de venda
preco_venda = calcular_preco_venda(50)

# Exibir os resultados
print(f"O preço de custo é: R$ {preco_custo:.2f}")
print(f"O preço de venda é: R$ {preco_venda:.2f}")







