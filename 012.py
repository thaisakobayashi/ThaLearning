"""Condições Aninhadas"""
"""Aninhar é quando você coloca uma coisa dentro da outra, vai encaixando as coisas
vai aninhando"""

# carro.siga()
# if carro.esquerda()  #se
# carro.siga()
# carro.direita()
# carro.esquerda()
# carro.siga()
# carro.direira()
# carro.siga()
# elif carro.direita() #senão se
# carro.siga()
# carro.esquerda()
# carro.siga()
# carro.esquerda()
# carro.siga()
# else:               #senão
#   carro.siga()
# carro.pare()

# if carro.esquerda():
"""bloco 1"""
# elif carro.direita():
"""bloco 2"""
# elif carro.ré():
"""bloco 3"""
# else:
"""bloco 4"""

#____________________________________________________________________________
# Prática
nome = str(input('Qual é o seu nome? '))
if nome == 'Thaisa':
   print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
   print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':
   print('Belo nome feminino')
else:
   print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))

# o if e elif funcionam sem o else, mas o elif não não funciona sem o if