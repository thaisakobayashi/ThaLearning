"""Manipulando Texto"""
# Para o Python toda cadeia de texto está entre aspas simples 'Curso em vídeo'
# Uma variável com uma string:
# frase = 'Curso em Vídeo Python'
# Onde a memória do computador vai criar espações para cada caractere da string
# A frase apresentada tem 21 espaços, pois a contagem começa do 0 e todos os
#  espaços são contados.
# __________________________________________________________________________

#OPERAÇÕES COM CADEIAS DE STRING

# Operação de Fatiamento, fatiar uma string é conseguir pegar pedaços dela
# FATIAMENTO
# frase[9]

frase = 'Curso em Vídeo Python'
frase[9]
print(frase[9]) # Quando usado assim, ele vai imprimir a letra que está no 9º espaço
print(frase[9:21])# Assim, ele vai imprimir do 9º espaço até o 21
print(frase[9:21:2])# E assim, ele vai imprimir a partir do 9 espaço
# porém, ele vai pulando de dois em dois, ignorando.
print(frase[:5])# Quando você coloca :5, o programa vai rodar do 0 até o espaço 5
# fatiando a palavra Curso
print(frase[15:])# E Quando você coloca 15:, o programa vai ler a partir do número
# escolhido, ou seja, do espaço 15 em diante, fatiando a palavra Python
print(frase[9::3])# Desse jeito, o programa irá fatiar, pulando dois, e colocando
# a terceira caractere
#________________________________________________________________________________
# 
# Operação de ANÁLISE

# Essa operação permite analisar uma string, como com que letra ela começa,com
# que letra ela termina, qual o tamanho dela, qual a primeira palavra inteira...

# Vamos então utilizar a função LEN (significa length: comprimento)
len(frase) # o len de frase seria 21, pois a frase possui 21 caracteres 
print(len(frase))

# Outra forma de analisar a string é utilizando o COUNT
frase.count('o')
print(frase.count('o')) # ele conta o número das letras 'o' existente na frase
frase.count('o',0,13)
print(frase.count('o',0,13)) # Aqui ele vai contar o número de 'o' do espaço 0
# até o espaço 13, que no caso considera até o 12, tendo só 1 letra 'o'

# LEMBRE-SE QUE O EM LETRA MAIÚSCULA É DIFERENTE DE o EM LETRA MINÚSCULA
print(frase.upper().count('O'))


#  Funcionalidade FIND, a funcionalidade utilizada para encontrar
frase.find('deo')
print(frase.find('deo')) # aqui ele vai mostrar o momento que começou o 'deo'
# ou seja, a posição da primeira letra, que seria o d na casa 11
# QUANDO VOCÊ QUER CONTAR A PRIMEIRA LETRA A PARTIR DE 1 E NÃO DO 0
# VOCÊ ACRESCENTA +1, OU SEJA, VAI FICAR:
#prim_pos_a = frase.lower().find('a')
# print('Aparece a primeira vez na posição: {}.'.format(prim_pos_a+1))
frase.find('Android')
print(frase.find('Android')) # quando você coloca uma palavra que não tem na
# frase, como a palavra 'Android', ele vai colocar -1, pois não foi encontrada
# Se eu pedir para ele procurar uma palavra existênte na frase, porém com
# a letra maiúscula ou minúscula, sendo o oposto, não vai achar
# Ex: vídeo com letra minúscula (na frase está com o V maiúsculo) para achar
# você vai precisar colocar: o 'lower'
print(frase.lower().find('vídeo'))

# Operador IN, não é uma funcionalidade, sim um operador, mas também da para
# utilizá-lo para análise
'Curso'in frase
print('Curso'in frase) # Aqui ele vai dizer se é verdadeiro ou falso, ou seja,
# vai dizer se tem ou não a palavra escolhida na frase
'Batata'in frase
print('Batata'in frase)

#______________________________________________________________________________

# Funcionalidade TRANSFORMAÇÃO

# Em via de regras, uma lista de string é imutavél, nós não conseguimos mexer nela
# Mas conseguimos mudar ela através dos métodos, não mexer direto nos elementos
# REPLACE
frase.replace('Python', 'Android')
print(frase.replace('Python', 'Android')) # Aqui ele vai procurar por Python
# e substituir pela palavra Android, porém só nessa instância, não vai salvar
# para salvar eu teria que criar a variável:
# frase = frase.replace('Python', 'Android')

# UPPER significa para cima
frase.upper() # é um método (Aqui ele vai colocar todas as letras que estavam
# em letras minúsculas em maiúsculas)
print(frase.upper())

# LOWER é o contrário do upper, aqui ele vai transformar todas as letras que 
# estiverem em maiúscula em minúscula
frase.lower()
print(frase.lower())

# O CAPITALIZE vai pegar uma string inteira, e deixar só a primeira letra maiúscula
# o resto ele vai mudar tudo para minúscula
frase.capitalize()
print(frase.capitalize())

# O TITLE vai colocar todas as palavras com letra inicial maiúscula
frase.title()
print(frase.title())

#___________________________________________________________________________

frase2 = '   Aprenda Python  '

# STRIP ele vai remover todos os espaços inúteis da frase, no ínicio e final
frase2.strip()
print(frase2.strip())

# De forma similar ao STRIP, nós temos o RSTRIP, com o r de right
frase2.rstrip() # Aqui ele vai remover os espaços da direita, mas vai manter
# os da esquerda
print(frase2.rstrip())

# LSTRIP vai manter os espaços da direita e remover os da esquerda
frase2.lstrip()
print(frase2.lstrip())
#____________________________________________________________________________

# Funcionalidades de DIVISÃO para dividir strings

# SPLIT (estudar sobre como fazer um split) DIVIDIR STRING EM LISTA
# Ele vai fazer a divisão das palavras, criando uma lista para cada uma, ou seja,
# cada palavra vai ter uma contagem. ['Curso'{0, 1, 2, 3, 4}. 'em'{0, 1}...]
# e todos esses espaços de palavras vai ter uma contagem:
# Curso: 0, em: 1, vídeo: 2, Python: 3.
frase.split()
print(frase.split())
dividido = frase.split()
print(dividido[0]) # aqui ele vai mostrar só o Curso, bloco 0
print(dividido[2][3]) # aqui ele vai pegar o bloco 2 que é Vídeo e vai mostrar a
# terceira letra, que é 'e'

# Quando você quer saber qual é o último bloco usa: 
# print('O último é: {}'.format(dividido[-1]))
#______________________________________________________________________________

# JUNÇÃO
frasex = frase.split()
# JOIN
# '-'.join(frase)
print('-'.join(frasex))
# Aqui ele vai separar a lista de palavras com traços - 

#___________________________________________________________________________
# Quando eu quero escrever uma frase bem grande eu abro print(""",jdjsfhd""")
# e coloco tudo entre 3 aspas duplas
print("""kfkjdashfdkjhfkjdshfkjdshfkjdhsfkjdhsfkjhdskjfhds
gdsyfgdsyugfsyudgfuysdgfyusdgfuygsdfuygdyfudgsyufgdshfiusdhf
sdhfiushfisudhfiushfisudhfidhusfsdiuhfsihfdhufihusdhfds
ufhsidhfsihfuisudhfdhusfihsdfsdufiusdhfiuhsdfihusdhfusdiuhfsiuh""")

