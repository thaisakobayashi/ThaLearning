"""Faça um programa que leia um número inteiro e diga se ele é ou não um 
número primo.""" #divisível por 1 e por ele mesmo

p = True
r = 0
n = int(input('Digite um número inteiro: '))
for c in range(2, 100):
   r = n % c
   if r == 0 and n != c:
      p = False
      print('O número {} é divisível pelo número {}, NÃO É PRIMO.'.format(n, c))
if p == True:
   print('É PRIMO!')

