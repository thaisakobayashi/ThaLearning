"""Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira."""

"""Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.""" #Olhar todas as classes no módulo math.

from math import trunc
n = float(input('Digite um número real: '))
ni = trunc(n)
ni2 = int(n)
print('O número Real {} tem a parte inteira {}.'.format(n, ni))
print(ni2)
#______________________________________________________
#Guanabara
#import math
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#ou se não quiser importar, pode usar o format(int(num))