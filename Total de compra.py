#Para calcular o total de uma compra em um supermercado, você deve declarar variáveis para os preços unitários dos produtos,
#solicitar ao usuário a quantidade de cada produto adquirido, calcular o total da comprar e exibir o resultado para o usuário.

preco_arroz = 10.00
preco_feijao = 8.50
preco_macarrao = 5.25

quantidade_arroz = int(input("Digite a quantidade de arroz: "))
quantidade_feijao = int(input("Digite a quantidade de feijão: "))
quantidade_macarrao = int(input("Digite a quantidade de macarrão: "))

TC = (preco_arroz * quantidade_arroz) + (preco_feijao * quantidade_feijao) + (preco_macarrao * quantidade_macarrao)

print("O total da compra é: ", TC)