#Código para saber se um número é par ou impar

n = int(input('Digite o número: '))

if n % 2 == 0: # se n é múltiplo de 2
  print(n, 'é par')

if n % 2 != 0: # se n não é múltiplo de 2
 print (n,'é impar')

 print('Fim.')