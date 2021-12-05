"""Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500."""


s = 0
for n in range(1, 500, 2):
   r = n % 3
   if r == 0:
      s = s + n
      print(s)
print('''A soma entre todos os números ímpares e múltiplos de três
é {}'''.format(s))