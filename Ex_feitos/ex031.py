"""Desenvolva um programa que pergunte a distância de uma viagem em km. 
Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km 
e R$0,45 para viagens mais longas."""

dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km!'.format(dist))
valor_200 = (dist * 0.50)
valor_201 = (dist * 0.45)
if dist <= 200:
   print('A sua passagem vai custar: R${:.2f}'.format(valor_200))
else:
   print('A sua passagem vai custar: R${:.2f}.'.format(valor_201))

# preco = dist * 0.50 if dist <= 200 else dist * 0.45 (MANEIRA SIMPLIFICADA)