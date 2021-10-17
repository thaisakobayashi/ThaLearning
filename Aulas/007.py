"""Operadores Aritméticos
+ : Adição; - : Subtração; * : Multiplicação; / : Divisão 
** : Potência; // : Divisão inteira; % : Resto da Divisão."""

"""5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1"""

"""Ordem de Precedência: 
1: ()
2: **
3: * , / , // , %
4: + , - """

"""Exemplos:
5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31 
3 * (5 + 4) ** 2 == 243
4**3 == 64
pow(4, 3) == 64 (perde a ordem de precedência)
81**(1/2) (raíz quadrada de 81)
21**(1/3) (raíz cubica de 21)"""


"""nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) # espaço de minímo de 20 digítos
# (Thaisa             ) 
print('Prazer em te conhecer {:>20}!'.format(nome)) # e alinhado a direita
# (              Thaisa)
print('Prazer em te conhecer {:<20}!'.format(nome)) # e alinhado a esquerda
# (Thaisa              )
print('Prazer em te conhecer {:^20}!'.format(nome)) # e centralizado
# (       Thaisa       )
print('Prazer em te conhecer {:=^20}!'.format(nome)) # centralizado e preenchido com "="
# (=======Thaisa=======)
print('Prazer em te conhecer {:->20}!'.format(nome)) # à direita e preenchido com "-"
# (--------------Thaisa)"""


n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2
rd = n1 % n2

print('=-'*30)
print('O calculo dos valores: {} e {} '.format(n1, n2))
print('A soma é {}, \no produto é {} e a divisão é {}'.format(s, m, d))
print('A divisão inteira é {}, a potência é {} e o resto da divisão é {}'.format(di, e, rd))
print('=-'*30)

print('A subtração é: {}'.format(n1 - n2), end=' - ')
print('A divisão é: {:.2f}'.format(d))
