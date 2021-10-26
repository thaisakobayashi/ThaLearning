"""Condições Parte 1 - Condições Simples e Compostas"""

"""Estruturas Condicionais"""

# Trabalhando com possibilidades

# Supondo que temos dois caminhos diferentes para o mesmo ponto de partida
# e o mesmo ponto de chagada de um carro, temos que criar em um mesmo programa
# dois, com as duas possibilidades, para a pessoa escolha o desejado.
# 
# Então para ao chegar na bifurcação, se a pessoa escolher o caminho da esquerda:

# carro.siga()
# se carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()
#   carro.direita()
#   carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()

# Ou caminho da direita:

# senão 
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
# carro.pare()

# O CARRO.SIGA() DO COMEÇO E O CARRO.PARE() DO FINAL, QUE ESTÃO UM POUCO MAIS
# A ESQUERDA, VÃO ACONTECER INDEPENDENTE DO CAMINHO ESCOLHIDO, DO CAMINHO "VERDE"
# OU "VERMELHO"

# VAMOS AGORA ORGANIZAR O COMANDO DESSA ESTRUTURA CONDICIONAL
#__________________________________________________________ # CONDIÇÃO:
# se carro.esquerda() se o carro for para a esquerda  # if carro.esquerda():
#    bloco_V_         faz o bloco verdadeiro          #   bloco True
# senão                                               # else:
# bloco_F_            faz o bloco falso               #   bloco False

# VAMOS UTILIZAR MUITAS ESTRUTURAS CONDICIONADAS,
# QUE NESSE CASO SERÁ O IF E O ELSE
# SOMENTE IF PARA ESTRUTURA SIMPLES E O IF E ELSE PARA ESTRUTURA COMPOSTA

tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:              # Se o tempo de vida do carro for de três anos...
   print('carro novo')
else:                     # Se o tempo de vida do carro for maior que três anos...
   print('carro velho')   
print('--FIM--')

# Esse programa funciona para duas situações, para a situação do carro ser novo
# ou do carro ser velho. Onde são dois fluxos, dois algoritmos, dois programas
# dentro de um só.

"""Todo comando que estiver colado do lado esquerdo da tela,
vai ser executado SEMPRE"""

"""E TODO COMANDO QUE ESTIVER ALINHADO ELE PODE SER EXECUTADO, OU NÃO
NUNCA VAI ACONTECER DE FUNCIONAREM AO MESMO TEMPO, OU É UM OU É OUTRO"""

# Outro jeito de fazer esse mesmo programa utilizando somente 3 linhas
# que é chamado de CONDIÇÃO SIMPLIFICADA 

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo<=3 else'carro velho')
print('--FIM--')

"""Condição simples:"""
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
   print('Que nome lindo você tem!') #Esse print só vai acontecer se o nome: Gustavo
print('Bom dia, {}!'.format(nome))
# t odos os prints colado no lado esquerdo sempre vão acontecer

"""Estrutura Composta"""
nome = str(input('Qual é o seu nome? '))
nome = nome.capitalize()
print(nome)
if nome == 'Thaisa':
   print('Que nome lindo você tem!')
else:
   print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome)) 

# Quando só tem o IF é uma condição SIMPLES
# Quando tem If e Else é uma condição COMPOSTA

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
   print('Sua média foi boa! PARANÉNS!')
else:
   print('Sua média foi ruim! ESTUDE MAIS!')

#PODEMOS FAZER DE UM MODO SIMPLIFICADO:

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2) / 2
# print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m>=6 else 'ESTUDE MAIS!') #CONDIÇÃO SIMPLIFICADA
