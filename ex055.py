"""Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos."""


maior = 0 
menor = 9999999
for c in range(0, 5):
   peso = float(input('Peso: '))
   if peso > maior:
      maior = peso
   if peso < menor:
      menor = peso
print(menor, maior)