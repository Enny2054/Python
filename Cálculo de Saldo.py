# Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano.
# Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela abaixo.
# Mostre uma mensagem informando o saldo médio e o valor do crédito.

def calcular_credito(saldo):
  if saldo < 200:
    print("Você não tem direito a crédito")
  elif saldo >= 200 and saldo <= 400:
      saldo_medio = 0.2 
  elif saldo >= 401 and saldo <= 600:
      saldo_medio = 0.3
  else: 
      saldo_medio = 0.4
  credito = saldo * (1 + saldo_medio)
  return credito 

saldo = float(input("Digite o valor do seu saldo médio: "))

resultado = calcular_credito(saldo)
print(f"Seu saldo médio é: R$ {saldo:.2f}")
print(f"Seu crédito é: R$ {resultado:.2f}")