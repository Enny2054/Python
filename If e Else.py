#Código criado para aprender o uso do if e else

cupom = input('Digite o cupom: ')

if (cupom == 'aula1' or cupom == 'aula2'):
  print('Cupom válido! Você ganhou 15% de desconto')

else:
 if(cupom != 'aula1' or cupom != 'aula2'):
   print('Cupom inválido! Você ganhou 10% de desconto')