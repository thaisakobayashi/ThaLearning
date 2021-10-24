"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro nome e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Segundo = Souza"""

nc = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
dividido = nc.split()
print('Seu primeiro nome é: {}'.format(dividido[0]))
print('Seu útimo nome é: {}'.format(dividido [-1]))

#___________________________________________________________________________
# GUANABARA
# n = str(input('Digite seu nome completo: ')).strip()
# nome = n.split()
# print('Seu 1º nome é: {}'.format(nome[0]))
# print('Seu último nome é: {}'.format(nome[len(nome)]-1))