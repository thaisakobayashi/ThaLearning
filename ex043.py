"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso/ (altura * altura)

if imc < 18.5:
   print('Seu IMC é {:.2f}. Você está abaixo do peso.'.format(imc))
elif 18.5 < imc <= 25:
   print('Seu IMC é {:.2f}. Parabéns! Você está com o peso ideal.'.format(imc))
elif 25 < imc <= 30:
   print('Seu IMC é {:.2f}. Você está com sobrepeso.'.format(imc))
elif 30 < imc <= 40:
   print('Seu IMC é {:.2f}. Você está Obeso(a).'.format(imc))
elif imc > 40:
   print('Seu IMC é {:.2f}. Você está com Obesidade mórbida.'.format(imc))
