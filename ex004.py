"""Faça um programa que leia algo pelo teclado e
mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele"""

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(algo)))
print('É alfabético: {}'.format(algo.isalpha()))
print('É numérico: {}'.format(algo.isnumeric()))
print('É um número decimal: {}'.format(algo.isdecimal()))
print('É alfabético e(ou) numérico: {}'.format(algo.isalnum()))
print('É espaço: {}'.format(algo.isspace()))
print('É minúsculo: {}'.format(algo.islower()))
print('É maiúsculo: {}'.format(algo.isupper()))
print('É titularizado: {}'.format(algo.istitle()))
