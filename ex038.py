"""Escreva um programa que leia os dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais."""

um = int(input('Digite um número inteiro: '))
dois = int(input('Digite mais um número inteiro: '))

if um > dois:
   print('O primeiro valor {}, é maior que o segundo.'.format(um))
elif dois > um:
   print('O segundo valor {}, é maior que o primeiro.'.format(dois))
elif um == dois:
   print('Não existe valor maior, os dois são iguais.')