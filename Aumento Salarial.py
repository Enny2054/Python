def aumento_salarial(salario, cargo):
  if cargo == "gerente" or "Gerente":
    aumento = 0.1
  elif cargo == "engenheiro" or "Engenheiro":
    aumento =  0.2
  elif cargo == "técnico" or "Técnico" or "Tecnico" or "tecnico":
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