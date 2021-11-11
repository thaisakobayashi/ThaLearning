"""A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER"""

ano_nasc = int(input('Ano de Nascimento: '))
soma = 2021 - ano_nasc

if soma <= 9:
   print('Sua categoria é MIRIM.')
elif 9 < soma <= 14:
   print('Sua categoria é INFANTIL.')
elif 14 < soma <= 19:
   print('Sua categoria é JUNIOR.')
elif 19 < soma <= 20:
   print('Sua categoria é SÊNIOR.')
elif soma > 20:
   print('Sua categoria é MASTER.')