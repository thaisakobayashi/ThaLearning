"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário 
escolher, só que agora utilizando um laço for."""

m = 0
n = int(input('Escolha entre 1 e 10, o número que você deseja saber a tabuada: '))
for c in range(0, 11):
   m = c * n
   print('{:2} x {:2} = {:2}'.format(n, c, m))