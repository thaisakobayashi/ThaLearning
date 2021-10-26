"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""

ano = int(input('Que ano deseja analisar? '))
div4 = ano % 4
div100 = ano % 100 
div400 = ano % 400
if div4 == 0:
   if div100 == 0:
      if div400 == 0:
         print('O ano {}, é Bissexto!'.format(ano))
      else:
         print('O ano {}, não é Bissexto!'.format(ano))
   else:
      print('O ano {}, é Bissexto!'.format(ano))
else:
   print('O ano {}, não é Bissexto!'.format(ano))

#____________________________________________________
# GUANABARA
#if ano % 4 == 0
#ano = int(input('Que ano quer analisar? '))
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#   print('O ano {} é BISSEXTO!'.format(ano))
#else: 
#   print('O ano {} NÃO é BISSEXTO!'.format(ano))

# if ano == 0
#from datetime import date
#ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
#if ano == 0:
#   ano = date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#   print('O ano {} é BISSEXTO!'.format(ano))
#else:
#   print('O ano {} não é BISSEXTO!'.format(ano))
