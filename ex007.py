"""Desenvolva um programa que leia as duas notas de um aluno, 
calcule e mostre a sua média."""

n1 = float(input('Nota um: '))
n2 = float(input('Nota dois: '))
s = n1 + n2
d = s / 2
print('A soma de {:.2f} + {:.2f} é {:.2f}'.format(n1, n2, s))
print('A média final é: {:.2f}'.format(d))
