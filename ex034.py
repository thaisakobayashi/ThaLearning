"""Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
- Para salários superiores a R$1.250,00, calcule um aumento de 10%.
- Para os inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Qual é o valor do seu salário? R$ '))
sal1 = sal / 100
sal10 = sal * 10
sal15 = sal1 * 15

if sal > 1250:
   sal_novo = sal + sal10
   print("""Se o seu salário for superior a R$1.250,00, você terá um aumento
   10%, passando o seu salário para R${:.2f}.""".format(sal_novo))
else:
   sal_novo = sal + sal15
   print("""Se o seu salário foi inferior a R$1.250,00, você terá um aumento
   de 15%, totalizando para R$ {:.2f}.""".format(sal_novo))

#___________________________________________________________________
# GUANABARA

# salário = float(input('Qual é o salário do funcionário? R$))
# if salário <= 1250:
   #novo = salário + (salário * 15 / 100)
# else:
   #novo salário + (salário * 10 / 100)
#print*'Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
#   
