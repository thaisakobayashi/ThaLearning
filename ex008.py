"""Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros."""

metros = float(input('Digite um valor em metros: '))
centimetros = 100 * metros
milimetros = 1000 * metros

print('\n')
print('O valor escolhido em metros é {:.2f}m'.format(metros)) 
print('Convertido em centímetros: {:.2f}cm'.format(centimetros)) 
print('E em milímetros: {:.2f}mm.'.format(milimetros))




