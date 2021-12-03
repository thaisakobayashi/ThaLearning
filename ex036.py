"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado."""
# valor da casa dividido pelo valor de parcelas

valor_casa = float(input('Valor da casa: R$ '))
valor_sal = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
parcelas = valor_casa / (anos * 12)
#parcelas = 12 * anos
sal_30 = valor_sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(parcelas))
if sal_30 <= parcelas:
   print('Infelizmente as parcelas no valor de R${:.2f}, excede 30% do seu salário. Sendo negado o seu empréstimo.'.format(parcelas))
elif sal_30 >= parcelas:
   print('O valor da sua prestação mensal será de R${:.2f}.'.format(parcelas))
#Guanabara:
if parcelas <= sal_30:
   print('Empréstimo CONCEDIDO!')
else:
   print('Empréstimo NEGADO!')