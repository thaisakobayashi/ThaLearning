"""Escreva um programa que pergunte a quantidade de km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por
km rodado."""

kmper = float(input('Quantidade de km percorridos: '))
qntd = int(input('Quantos dias de aluguel: '))
sdia = 60 * qntd
kmrod = 0.15 * kmper
total = sdia + kmrod

print('Com a quantidade de {} dia(s) de aluguel, o total é de R${:.2f}.'.format(qntd, sdia))
print('Com {}km percorridos, o valor total de km rodados é de R${:.2f}.'.format(kmper, kmrod))
#não precisa colocar os print's acima, na correção pode colocar só
#as duas primeiras variáveis com o último print.
print('___________________________________________________')
print('O total a pagar é de R${:.2f}.'.format(total))