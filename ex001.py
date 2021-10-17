"""Crie um script Python que leia o nome de uma pessoa e 
mostra uma mensagem de boas-vindas de acordo com o valor digitado"""

nome = input('Qual é o seu nome? ')
print('Seja bem-vindo,' , nome, '!')

print('Olá' , nome, '!', 'Prazer em te conhecer!')

neko = input('Qual é o nome do seu gato? ')
mel = input('Qual é o nome da sua gata? ')
print('Olá' , nome, '!' , 'O' , neko, 'e a' , mel , 'são muito fofinhos!' )

print('É um prazer te conhecer {}!'.format(nome))
print('Olá {}! O {} e a {} são muito fofinhos!'.format(nome, neko, mel))