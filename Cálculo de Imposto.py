# Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa de 1% para carros fabricados antes de 1990 
# e uma taxa de 1.5% para os fabricados de 1990 em diante, a taxa está incidindo sobre o valor do carro. 
# Faça uma algoritmo lê o ano e o preço do carro e a seguir calcula e imprime o imposto a ser pago.

def calcular_imposto(ano, preco):
  if ano < 1990:
    taxa = 0.01
  else:
    taxa = 0.015

    imposto = preco * taxa
  return imposto

ano = int(input("Digite o ano de fabricação do carro: "))
preco = float(input("Digite o preço do carro: "))

resultado = calcular_imposto(ano, preco)

print(f"O imposto a ser pago é: R$ {resultado:.2f}")