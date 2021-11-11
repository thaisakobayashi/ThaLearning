"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite."""

v = float(input('Qual a velocidade atual do carro: '))
print('Tenha um bom dia! Dirija com segurança!')
sub = (v - 80)
multa = sub * 7
if v > 80:
   print('Você foi multado! A multa vai custar R${:.2f}!'.format(multa))

