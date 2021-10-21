"""Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raíz quadrada."""

n1 = float(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
e = n1 ** 2
r = n1 ** (1/2)

print('O dobro do número {:.2f} é {:.2f}, \nsendo seu triplo {:.2f}, \nsua elevação ao quadrado {:.2f} \ne sua raíz quadrada {:.2f}.'.format(n1, d, t, e, r))
