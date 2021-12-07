"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

#dando errado
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
for c in range(pt, r * 11, r):
   print(c, end=' ')


#Guanabara CERTO
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão 
for c in range(primeiro, decimo + razão, razão):
   print('{}'.format(c), end='- ')
print('ACABOU')