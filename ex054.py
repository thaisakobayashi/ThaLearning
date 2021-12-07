"""Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
já são maiores.""" #considere a maioridade 21 anos


menor = 0
maior = 0
for c in range(0, 7):
   ano = int(input('Ano de nascimento: '))
   if 21 > 2021 - ano:
      menor = 1 + menor
   else:
      maior = maior + 1 
print('{} pessoas são maiores de idade.'.format(maior))
print('{} pessoas são menores de idade.'.format(menor))

#Guanabara
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
   nasc= int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
   idade = atual - nasc
   if idade >= 21:
      tot +=1
   else:
      totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
