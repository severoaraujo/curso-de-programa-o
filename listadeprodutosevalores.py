#listadeprodutosevalores
produtos=["arroz","feijao","cuscus"]
valores=[10, 8.7, 2.50]
quantidade=[10,5,5]

for i in range(len(produtos)):
    produto= produtos [i]
    valor =valores [i]
    qdt= quantidade[i] 
    print(produto,valor,qdt, valor*qdt)