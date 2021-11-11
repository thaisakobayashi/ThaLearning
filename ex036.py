"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado."""
# valor da casa dividido pelo valor de parcelas

valor_casa = float(input('Qual é o valor da casa? '))
valor_sal = float(input('Qual é o seu salário? '))
anos = float(input('Em quantos anos deseja pagar o valor total da casa? '))
parcelas = 12 * anos
sal_30 = valor_sal * 30 / 100

if sal_30 < parcelas:
   print('Infelizmente as parcelas no valor de R${}, excede 30% do seu salário. Sendo negado o seu empréstimo.'.format(parcelas))
elif sal_30 > parcelas:
   print('O valor da sua prestação mensal será de R${}.'.format(parcelas))