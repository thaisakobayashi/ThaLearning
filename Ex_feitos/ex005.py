"""Faça um programa que leia um número inteiro 
e mostre na tela o seu sucessor e seu antecessor"""


n1 = int(input('Digite um número inteiro: ')) 
sucessor = n1 + 1
antecessor = n1 - 1
print('O número {}: \nTêm como seu antecessor {}, \ne tem como seu sucessor: {}.'.format(n1, antecessor, sucessor))

