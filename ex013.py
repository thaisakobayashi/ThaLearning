"""Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento."""

salario = float(input('Digite o valor do seu salário atual: R$'))
sal1 = salario / 100
sal15 = sal1 * 15
novosal = salario + sal15

print('O valor do seu sálario é de R${:.2f}.'.format(salario))
print('Você terá um acréssimo de R${:.2f}'.format(sal15))
print('Com o aumento de 15%, seu salário irá subir para R${:.2f}.'.format(novosal))
