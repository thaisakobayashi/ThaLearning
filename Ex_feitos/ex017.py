"""Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retânguro, calcule e mostre o comprimento da 
hipotenusa.""" 

#Teorema de Pitágoras sqrt(x*x + y*y)

from math import hypot, sqrt
catetoop = float(input('O comprimento do cateto oposto é: '))
catetoad = float(input('O comprimento do cateto adjacente é: '))
hip = sqrt(catetoop * catetoop + catetoad * catetoad)
hip2 = (catetoop ** 2 + catetoad ** 2)**(1/2)
hip3 = hypot(catetoop, catetoad)
print('O valor da hipotenusa é de {:.2f}.'.format(hip))
print('A hipotenusa vai medir: {:.2f}'.format(hip2))
print('A hipotenusa vai medir: {:.2f}.'.format(hip3))

