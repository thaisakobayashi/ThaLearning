""""Faça um programa que leia uma frase pelo teclado e mostre:
-> Quantas vezes aparece a letra "A".
-> Em que posição ela aparece a primeira vez.
-> Em que posição ela aparece a última vez."""

frase = str(input('Digite uma frase: ')).strip()
quant_a = frase.upper().count('A')
prim_pos_a = frase.lower().find('a')
ult_pos_a = frase.lower().rfind('a')
print('A letra A aparece {} vezes na frase.'.format(quant_a))
print('Aparece a primeira vez na posição: {}.'.format(prim_pos_a+1))
print('Última vez que A aparece, é na posição: {}.'.format(ult_pos_a+1))


#________________________________________________________________________
# GUANABARA
# frase = str(input('Digite uma frase: ')).upper().strip() 
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}'.format(frase.find('A)+1))
# print('A última letra A apareceu na posição {}'.format(frase.rfind('A)+1))