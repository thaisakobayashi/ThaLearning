"""Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.
- O programa deverá escrever na tela se o usuário venceu ou perdeu.""" 

num = int(input('Entre 0 e 5, qual número você acha que o computador vai escolher? '))
import random
n = random.randint(0, 5)
print('O número escolhido pelo computador foi: {}.'.format(n))
if num == n:
   print('Parabéns! VOCÊ VENCEU!!!')
else: 
   print('VOCÊ PERDEU! Tente novamente! Eu pensei no número {} e não no {}'.format(n, num))

#_________________________________________________________________
#GUANABARA
# from random import randint
# from time import sleep
# computador = randint(0, 5)
# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# print('-=-' * 20)
# jogador = int(input('Em que número eu pensei?')) # jogador tenta adivinhar
# print('PROCESSANDO...')
# sleep(3)
# if jogador == computador:
   #print('PARABÉNS! Você conseguiu vencer!')
#else:
   #print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
