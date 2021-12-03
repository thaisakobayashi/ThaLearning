"""Escreva um programa que leia os dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais."""

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))

if n1 > n2:
   print('O primeiro valor {}, é maior que o segundo.'.format(n1))
elif n2 > n1:
   print('O segundo valor {}, é maior que o primeiro.'.format(n2))
elif n1 == n2:
   print('Não existe valor maior, os dois números são IGUAIS.')

#ou:
# else
#    print('Os dois valores são iguais!')