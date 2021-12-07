"""Faça um programa que leia um número inteiro e diga se ele é ou não um 
número primo.""" #só é divisível por 1 e por ele mesmo

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


#Guanabara
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
   if num % c == 0:
      print('\033[33m', end=' ')
      tot += 1
   else:
      print('\033[31m', end=' ')
   print('{}'.format(c, end=' '))
print('\n\033[m0 número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
   print('E por isso ele é PRIMO!')
else:
   print('E por isso ele NÃO É PRIMO!')
