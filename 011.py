"""Cores no Terminal"""

# \033[0:33:44m 

# style back text
#  0     33   44

# Style: 0 none, 1 bold, 4 underline, 7 negative

# Text: 30 branco; 31 vermelho; 32 verde, 33 amarelo, 34 azul,
#  35 roxo, 36 azul bebê, 37 cinza

# Back: 40 fundo branco, 41 f vermelho, 24 f verde,
#  43 f amarelo, 44 f azul, 45 f roxo, 46 f azul bebê, 47 f cinza.

# Teste \033[0;30;41m fundo vermelho letra branca
# Teste \033[4;33;44m fundo azul, letra amarela sublinhada
# Teste \33[1;35;43m fundo amarelo letra roxa
# Teste \33[30;42m fundo verde letra branca
# Teste \033[m fundo preto letra branca
# Teste \033[7;30m fundo branco letra preta

#print('\033[1;33;40mOlá Mundo!')

#30      black       preto      40
#31      red         vermelho   41
#32      green       verde      42
#33      yellow      amarelo    43
#34      blue        azul       44
#35      Magenta     Magenta    45
#36      cyan        ciano      46
#37      grey        cinza      47
#97      white       branco     107

#a = 3
#b = 5
#print('Os valore são \033[33m{}\033[m e \033[31m{}\033[m!!'.format(a, b))

nome = 'Thaisa'
cores = {'limpa';'\033[m',
'azul;';'\033[34m',
'amarelo';'033[33m',
'pretobranco';'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))