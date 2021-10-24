'''Utilizando Módulos - Biblioteca'''

#adicionando recursos (módulos) no pyton, onde cada grupo chamamos de
#biblioteca

#ex:
#bebida: suco, refri, milkshake, água
#comida: pizza, cachorro quente, lanche, ovo
#doce: trudel, brigadeiro, pudim, bolo, sorvete
# Cada grupo desses chamamos de biblioteca

#Na programação podemos fazer importações a esse ripo de biblioteca
#Assim importando de fora
# Ou seja, posso usar um comando 'import(bebida(suco, refri, milkshake, água))
#e todos os itens dentro da biblioteca 'bebida' serão importados automaticamente.
#porém se eu quiser da biblioteca de doce SOMENTE o trudel, antes da palavra doce
#eu vou colocar 'from(doce(import(trudel))) só importando o item desejado.

#_______________________________________________________________________________
#from typing import Match
#import(bebida) IMPORTA TODAS AS FUNCIONALIDADES DESCRITAS ACIMA
#from(doce(import))IMPORTA APENAS AS FUNCIONALIDADES QUE EU ESCOLHER

#Uma biblioteca padrão muito utilizada é a 'math', que significa matemática.
#Então ela vai trazer algumas funcionalidades matemáticas extras.
#math
#Como por exemplo, uma funcionalidade que o math trás é o 'ceil'
#Que é quando você tem a nota de um aluno e quer arredondar ela para cima
#Ou a funcionalidade 'floor' que arredonda para baixo.
#a funcionalidade 'trunc' vai truncar o número, eliminar da vírgula para
#frente, sem fazer arredondamento nenhum.
#funcionalidade 'pow' que é potência, vai funcionar de maneira semelhante
#aos dois **
#funcionalidade 'sqrt' usada para calcular a raíz quadrada
#funcionalidade 'factorial' 
#Se você usar o comando 'import(math)' ele vai importar todas as funcionalidades
#acima
#import math
#Agora see você quiser utilizar apenas uma funcionalidade, ai você vai
#utilizar o comando:
#from math import sqrt
#ou se quiser mais de uma: from math import sqr, ceil
#_______________________________________________________________________
#Prática
#Para você utilizar a biblioteca, você deve colocar antes o que quer importar:
import math
#Vou pedir para ler um número:
num = int(input('Digite um número:'))
#Agora eu quero a raíz quadrada desse número
raiz = math.sqrt(num)
print('A raíz de {} é igual a {:.2f}'.format(num, raiz))
#Você pode arredondar a raíz para cima usando:
print('A raíz de {} é igual a {}'.format(num, math.ceil(raiz)))
#Se quiser arredondar para baixo:
print('A raíz de {} é igual a {}'.format(num, math.floor(raiz)))

#Agora utilizando:
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual a {:.2f}.'.format(num, raiz))

#Se eu quiser posso importar o sqrt e o floor também, sendo assim:
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual a {:.2f}.'.format(num, floor(raiz)))

#___________________________________________________________________________
#As bibliotecas que eu posso acessar (site):
#python.org (entrando no site, clique em docs, para escoher a versão)
#Veja aqui no pycharm a versão, clicando em Python Console, que fica 
#no lado esquerdo, debaixo da tela (Python 3.9.5), selecione no site a versão
#Depois de selecionado, vá em Library Reference (Referência da Biblioteca)

#_________________________________________________________________________
#Continua no 008+.py
#import random
# num = random.randint(1, 10)
#__________________________________________________________________________

#import emoji
#print(emoji.emojize("Olá, Mundo: earth_americans"))



