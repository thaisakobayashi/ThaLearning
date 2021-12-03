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


#GUANABARA
#print('{:=40}'.format(' LOJAS GUANABARA '))
#preco = float(input('Preço das compras: R$'))
#print('''FORMAS DE PAGAMENTO
#[ 1 ] à vista dinheir/cheque
#[ 2 ] à vista cartão
#[ 3 ] 2x no cartão
#[ 4 ] 3x ou mais no cartão''')
#opcao = int(input('Qual é a opção? '))
#if opcao == 1:
#   total = preco - (preco * 10 / 100)
#elif opcao == 2:
#   total = preco - (preco * 5 / 100)
#elif opcao ==3:
#   total = preco
#   parcela = total / 2
#   print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
#elif opcao ==4:
#   total = preco + (preco * 20 / 100)
#   totparc = int(input('Quantas parcelas? '))
#   parcela = total / totparc
#   print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparc, parcela))
#else:
#   total = 0
#   print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
#print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))