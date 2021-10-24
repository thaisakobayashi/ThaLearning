""""Crie um programa que leia o nome da pessoa e
diga se ela tem 'SILVA' no nome."""

name = str(input('Nome completo: ')).strip()
print('O nome completo é: {}'.format(name.title()))
nome_minus = name.lower()
silva = 'silva' in nome_minus
print('Silva compõe o seu nome? {}'.format(silva))

#___________________________________________________________________________
# GUANABARA
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))