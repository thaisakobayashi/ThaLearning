'''Laços de Repetição (Parte I)'''

#laço c no intervalo(1,10)
#   passo
#pega
#=
#for c in range(1,10):
#   passo
#pega

#comando para pular 
#laço c no intervalo(0,3)
#   passo
#   pula
#passo
#pega

#for c in range(0,3):
#   passo
#   pula
#passo
#pega

#for c in range(0,3):
#   if moeda:
#      pega
#   passo
#   pula
#passo
#pega


"""for c in range(1, 6): #quando você coloca de um até 6, o último ele ignora
   print('Oi')
   print('FIM')

for c in range(1, 6):
   print('Oi')
print('FIM')

print('---------------------------')"""

for c in range(0, 7, 2): #aqui ele conta até 6, pulando de 2 em 2
   print(c)
print('FIM\n')

n = int(input('Digite um número: '))
for c in range(0, n+1):
   print(c)
print('FIM\n')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
   print(c)
print('FIM\n')

for c in range(0, 2):
   n = int(input('Digite um valor: '))
print('Fim\n')

s = 0
for c in range(0, 4):
   n = int(input('Digite um valor: '))
   s += n
print('O somatório de todos os valores foi {}'.format(s))