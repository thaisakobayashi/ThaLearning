"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor
de seno, cosseno e tangente desse ângulo.""" #seno vertical, cosse horiz

import math 
ang = float(input('Ângulo: '))
seno = math.sin(math.radians(ang)) 
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, coss))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tang))