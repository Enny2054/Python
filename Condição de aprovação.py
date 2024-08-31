#Peça ao usuário para digitar uma nota (de 0 a 100) e classifique a nota em uma das categorias:
# Aprovado, Recuperação ou Reprovado.

nota = int(input("Digite a nota: "))

if (nota >= 70):
  print("Aprovado")
else:
  if ( nota >= 40 and nota <= 69):
    print("Recuperação")
  else:
    print("Reprovado")
