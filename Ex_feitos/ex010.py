"""Crie um programa que leia quanto dinheiro uma pessoa tem 
na carteira e mostre quantos dólares ela pode comprar.
Considere
US$1,00 = R$3,27""" """18/10/2021 - US$1,00 = R$5,46"""

carteira = float(input('Digite o valor em reais que você possui na sua carteira: '))
dolar_antigo = carteira / 3.27
dolar_atual = carteira / 5.46

print('Com o valor de R${}, você pode comprar US${:.2f} do dólar antigo e US${:.2f} do dólar atual.'.format(carteira, dolar_antigo, dolar_atual))
