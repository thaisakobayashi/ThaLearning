"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

preco = float(input('Preço do produto: '))
forma_pag = int(input('''Digite o número da opção de pagamento: 
                           \n1- Dinheiro
                           \n2- Cartão
                           \n3- Em até 2x
                           \n4- Em 3x ou mais: \n \n'''))
dinheiro = preco - (10 * preco / 100)
cartao_a_vista = preco - (5 * preco / 100)
em_2x = preco
x3_ou_mais = preco + (20 * preco / 100)

if forma_pag == 1:
   print('Seu produro ficou por R${:.2f}, com 10% de desconto.'.format(dinheiro))
elif forma_pag == 2:
   print('Seu produto ficou por R${:.2f}, com 5% de desconto.'.format(cartao_a_vista))
elif forma_pag == 3:
   print('Seu produto ficou por R${:.2f}.'.format(em_2x))
elif forma_pag == 4:
   print('Seu protudo ficou por R${:.2f}, com 20% de juros.'.format(x3_ou_mais))
else:
   print('Desculpe, você precisa digitar o número da opção de pagamento.')
