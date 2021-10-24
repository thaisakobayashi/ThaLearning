"""Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas
-> O nome com todas minúsculas
-> Quantas letras ao todo (sem considerar espaços)
-> Quantas letras tem o primeiro nome"""

nc = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é: {}'.format(nc.upper()))
print('Seu nome em minúsculo é: {}'.format(nc.lower()))
lista_nome = nc.split()
nome_junto = ''.join(lista_nome)
print('Seu nome ao todo tem {} letras.'.format(len(nome_junto)))
print('Seu primeiro nome tem {} letras.'.format(len(lista_nome[0])))

#_______________________________________________________________________
# Guanabara
# nome = str(input('Digite seu nome completo: ')).strip()
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))