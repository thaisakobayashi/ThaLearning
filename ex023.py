"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados
Ex: 
Digite um número: 1834

Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1"""

n = int(input('Digite um número de 0 a 9999: '))
print('O número digitado é: {}'.format(n))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print('Analisando o número {}...'.format(n))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

#__________________________________________________________
# OTAVIO
n = '{:4}'.format(n)
u = n[3]
d = n[2]
c = n[1]
m = n[0]
d = d.replace(' ', '0')
c = c.replace(' ', '0')
m = m.replace(' ', '0')
print('Analisando o número {}...'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))