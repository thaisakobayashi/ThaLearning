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

