"""Faça um algoritmo que leia o preço de um produto e 
mostre seu novo preço, com 5% de desconto."""

preco = float(input('Digite o preço do produto: R$ '))
preco1 = preco / 100
preco5 = preco1 * 5
precod = preco - preco5

print('O preço do produto é: R${:.2f}'.format(preco))
print('Desconto ganho com 5%: R${:.2f}'.format(preco5))
print('O valor final com o desconto é de: R${:.2f}'.format(precod))