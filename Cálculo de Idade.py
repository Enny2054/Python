idade = int(input("Digite a sua idade: "))

if ( idade <= 12):
  print("Você está no grupo infantil")
else:
  if ( idade >= 13 and idade <= 17):
    print("Você está no grupo juvenil")

  else:
    if ( idade >= 18 and idade <= 65):
     print("Você está no grupo adulto")

    else:
      print("Você está na idoso")