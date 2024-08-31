#Crie um código que peça ao usuário para digitar uma senha e verifique se a senha está correta. 
#Se a senha estiver correta, exiba uma mensagem de boas-vindas; caso contrário, informe que a senha está incorreta.

senha = int(input("Digite a senha: "))

if ( senha == 2054):
  print("Bem vindo!")
else:
  print("Senha incorreta")