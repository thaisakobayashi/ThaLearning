"""Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com o nome 'SANTO'."""

cid = str(input('Digite o nome de uma Cidade: ')).strip()
print('O nome da Cidade é: {}'.format(cid.title()))
lista_nome = cid.split()
cid_minus = cid.lower()
santo = 'santo' in cid_minus
print('Ela começa com Santo? {}'.format(santo))


#____________________________________________________________
# GUANABARA
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')