"""Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500."""


s = 0
for n in range(1, 500, 2):
   r = n % 3
   if r == 0:
      s = s + n
      print(s, end=' ')
print('''A soma de todos os números ímpares e\n múltiplos de três é {}'''.format(s))



#Guanabara 
soma = 0
cont = 0
for c in range(1, 501, 2):
   if c % 3 == 0:
      soma += c
      cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))