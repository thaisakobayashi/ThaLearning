#Continuação da aula 008

#Importando da biblioteca random
#Na biblioteca random eu posso gerar números aleatórios 

import random
num = random.random()
print(num)

#Ao invés de eu utilizar o input, para pedir para alguém me falar um número
#vou usar o random.random para o computador me dar um número aleatório.
#____________________________________________________________________________

#Se eu quiser também, posso pedir para o computador gerar um número inteiro
#de 1 a 10, usando:

import random
num = random.randint(1, 10)
print(num)

#Ainda no site, você pode ir em: PyPi, que é: índice de pacotes extras
#que pode ser importado separadamente. 

import emoji
print(emoji.emojize("Olá, Mundo :sunglasses: :earth_americas:", use_aliases=True))

print(emoji.emojize('Nós somos o Neko :cat: e a Mel :cat:', use_aliases=True ))

#Para ver os emojis tem que ir na biblioteca: emoji 1.6.1
#Ir em links: Emoji Cheat Sheet


#Para instalar uma biblioteca você precisa colocar no terminal:
#pip install 'e o nome da biblioteca'
#Se o pip não estiver instalado, o comando para instalar é: 
#sudo apt install python3-pip
