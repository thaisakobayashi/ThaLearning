"""Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou de prazo."""

ano = float(input('Em que ano você nasceu? '))


if 2021 - ano == 18:
   print('Está na hora de se alistar.')
elif 2021 - ano < 18:
   print('Você vai se alistar ao serviço militar, mas ainda não chegou a hora.')
elif 2021 - ano > 18:
   print('Você já passou do seu tempo de alistamento.')

#Guanabara

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
   print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
   saldo = 18 - idade
   print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
   ano = atual + saldo
   print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
   saldo = idade - 18
   print('Você já deveria ter se alistado há {} anos.'.format(saldo))
   ano = atual - saldo
   print('Seu alistamento foi em {}'.format(ano))