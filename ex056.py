"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre: 
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos."""

s = 0
maior = 0
mulheres_menor = 0 
for c in range(0, 4):
   nome = input('Nome: ')
   idade = int(input('Idade: '))
   sexo = input('Sexo: ')
   s = s + idade
   if sexo == 'm' and idade > maior:
      maior = idade
   if sexo == 'f' and idade < 20:
      mulheres_menor = mulheres_menor + 1 
media = s / 4 
print('A média é {}'.format(media))
print('O nome do homem mais velho é {}.'.format(maior)) #NÃO COLOQUEI NOME
print('Têm {} mulheres com menos de 20 anos.'.format(mulheres_menor))
