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


#GUANABARA
#from random import randint
#itens = ('Pedra', 'Papel', 'Tesoura')
#computador = randint(0, 2)
#print('''Suas opções:
#[ 0 ] PEDRA
#[ 1 ] PAPEL
#[ 2 ] TESOURA''')
#jogador = int('Qual é a sua jogada? ')
#print('-=' * 11)
#print('O computador jogou {}'.format(itens[computador]))
#print('O jogador jogou {}'.format(itens[jogador]))
#print('-=' * 11)
#if computador == 0: PEDRA
#   if jogador == 0:
#      print('EMPATE')
#   elif jogador == 1:
#      print('JOGADOR VENCE!')
#   elif jogador == 2:
#      print('COMPUTADOR VENCE!') 
#   else:
#      print('JOGADA INVÁLIDA!')
#elif computador == 1: PAPEL
#   if jogador == 0:
#     print('JOGADOR VENCE!')
#   elif jogador == 1:
#       print('COMPUTADOR VENCE')
#   elif jogador == 2:
#      print('EMPATE')
#   else:
#       print('JOGADA INVÁLIDA)
#elif computador == 2: TESOURA 
#   if jogador == 0:
#     print('JOGADOR VENCE')
#   elif jogador == 1:
#      print('COMPUTADOR VENCE')
#   elif jogador == 2:
#      print('EMPATE')
#   else:
#       print('JOGADA INVÁLIDA!')