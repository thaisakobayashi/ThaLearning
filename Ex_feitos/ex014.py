"""Escreva um programa que converta uma temperatura digitada em ºC 
e converta para ºF."""

grauc = float(input('Informe a temperatura em ºC: '))
grauf = grauc * 9 / 5 + 32

print('A temperatura de {} corresponde a {}ºF.'.format(grauc, grauf))
