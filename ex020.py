"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalho dos alunos. Faça um programa que leia o nome dos quatro
alunos e mostre a ordem sorteada."""

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
ordem = lista
print('A ordem de apresentação dos alunos será: {}'.format(ordem))

#Se não quise colocar a variável 'ordem', é só colocar no format(lista) 