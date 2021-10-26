"""Crie um programa que leia um número inteiro e mostre na tela se ele é 
PAR ou IMPAR."""

n = int(input('Me diga um número qualquer: '))
r = n % 2 
if r == 0:
   print('O número {} é par!'.format(n))
else:
   print('O número {} é impar!'.format(n))


# o resto de qualquer número par dividido por 2 é 0
# e o resto de qualquer número ímpar dividido por 2 é 1

