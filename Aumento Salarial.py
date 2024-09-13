# Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo.
# Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário. 
# Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento. 
# Mostre o salário antigo, o novo salário e a diferença.

def aumento_salarial(salario, cargo):
  if cargo == "gerente" or "Gerente" or 101:
    aumento = 0.1
  elif cargo == "engenheiro" or "Engenheiro" or 102:
    aumento =  0.2
  elif cargo == "técnico" or "Técnico" or "Tecnico" or "tecnico" or 103:
    aumento = 0.3
  else:
   aumento = 0.4
    
  novo_salario = salario * (1 + aumento)
  return novo_salario

salario = float(input("Digite o valor do seu salário: "))
cargo = input("Digite o seu cargo: ")

resultado = aumento_salarial(salario, cargo)
diferenca = resultado - salario

print(f"O seu antigo salário é: R$ {salario:.2f}")
print(f"Agora seu novo salário é: R$ {resultado:.2f}")
print(f"Você teve um aumento salarial de: R$ {diferenca:.2f}")
