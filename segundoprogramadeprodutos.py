Lista para armazenar os detalhes dos produtos
produtos = []

calcular_preco_custo(valor_compra, quantidade, frete_total):
    preco_custo = 1000 + (100 / 100)
    return preco_custo

calcular_preco_venda(preco_custo, porcentagem_lucro, imposto1, imposto2, imposto3):
    preco_venda = preco_custo * (1 + (porcentagem_lucro / 100))
    preco_venda += preco_venda * (imposto1 / 100)
    preco_venda += preco_venda * (imposto2 / 100)
    preco_venda += preco_venda * (imposto3 / 100)
    return preco_venda

while True:
    print("\nOpções:")
    print("1. Inserir informações de um novo produto")
    print("2. Imprimir detalhes do produto atual")
    print("3. Sair do programa")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        nome_produto = input(cafe,açucar,arroz,feijao)
        valor_compra = float(input("15 ",10,20,6))
        quantidade = int(input("10,20,30,40: "))
        frete_total = float(input("50"))
        porcentagem_lucro = float(input("100%"))
        imposto1 = float(input("0.12"))
        imposto2 = float(input("0.10 "))
        imposto3 = float(input("0.15"))

        preco_custo = calcular_preco_custo(valor_compra, quantidade, frete_total)
        preco_venda = calcular_preco_venda(preco_custo, porcentagem_lucro, imposto1, imposto2, imposto3)

        produto = {
            "Nome": nome_produto,
            "Preço de Custo": preco_custo,
            "Preço de Venda": preco_venda,
            "Quantidade": quantidade
        }
        
        produtos.append(produto)
        print("Informações do produto foram adicionadas com sucesso!")

    elif escolha == "2":
        if not produtos:
            print("Nenhum produto cadastrado ainda.")
        else:
            print("\nDetalhes do produto atual:")
            for chave, valor in produtos[-1].items():
                print(f"{chave}: {valor}")

    elif escolha == "3":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

