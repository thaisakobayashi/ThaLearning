"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar. desconsidere-o."""

s = 0
r = 0
for c in range(0, 6):
   n = int(input('Digite um número inteiro: '))
   r = n % 2
   if r == 0:
      s = n + s
      print(s)

#Guanabara
soma = 0 #SOMAR
cont = 0 #CONTAR
for c in range(1, 7):
   num = int(input('Digite o {} valor: '.format(c)))
   if num % 2 == 0: #PAR
      soma += num   #simplificando soma = soma + num por += num
      cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))