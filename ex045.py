"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import choice 

(print('Vamos jogar Jokenpô!'))
n = (input('Você quer pedra, papel ou tesoura? '))
mylist = ["pedra", "papel", "tesoura"]
computador = choice(mylist)
print('Eu escolhi {} e você {}, então...'.format(computador, n))

if computador == "pedra": 
   if n == "pedra":
      print('Empatamos!')
   elif n == "papel":
      print('Parabéns! Você ganhou!')
   elif n == "tesoura":
      print('Você perdeu!')
elif computador == "papel":
   if n == "pedra":
      print('Você perdeu!')
   elif n == "papel":
      print('Empatamos!')
   elif n == "tesoura":
      print('Parabéns! Você ganhou!')
elif computador == "tesoura":
   if n == "pedra":
      print('Parabéns! Você ganhou!')
   elif n == "papel":
      print('Você perdeu!')
   elif n == "tesoura":
      print('Empatamos!')

