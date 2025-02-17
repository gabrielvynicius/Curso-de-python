from random import choice
a1 = str(input('Primeiro Pessoa: '))
a2 = str(input('Segundo Pessoa: '))
a3 = str(input('Terceiro Pessoa: '))
a4 = str(input('Quarto Pessoa: '))
a5 = str(input('Quinta Pessoa: '))
a6 = str(input('Sexta Pessoa: '))
ganhador = [a1, a2, a3, a4, a5, a6]
print('A pessoa que ganhou R$ 100.000,00 foi {}.'.format(choice(ganhador)))
