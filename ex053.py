"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.""" #é aquela frase que lemos de trás para a frente

"""Ex: 
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA"""

#frase = 'jorge é carro'.split()
#frase = ''.join(frase)
#frasec = ''
#print(frase)
#letras = len(frase)
#for l in range(0, letras + 1):
#   frase[l]
#   print(frase[l])

#Guanabara
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
   inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
   print('Temos um palíndromo!')
else:
   print('A frase não é um palíndromo!')

#Sem o for
#frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''[::-1]
if inverso == junto:
   print('Temos um palíndromo!')
else:
   print('A frase não é um palíndromo!')