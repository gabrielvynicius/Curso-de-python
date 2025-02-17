''' from random import sample
q1 = str(input('Digite algo que deseja conquistar: '))
q2 = str(input('Digite algo que deseja conquistar: '))
q3 = str(input('Digite algo que deseja conquistar: '))
q4 = str(input('Digite algo que deseja conquistar: '))
conquistas = [q1, q2, q3, q4]
print('Se você for tentar fazer tudo de uma vez pode não da certo,\n'
      'Porém se voce conquistar um por vez, vai ser melhor.\n'
      'E pra te ajudar ja escolhi a sequencia das suas conquistas:\n'
      '{}\n'
      'Agora é so correr atrás. '.format(sample(conquistas, len(conquistas))))'''
from random import shuffle
p1 = str(input('Digite o nome de uma pessoa:'))
p2 = str(input('Digite o nome da segunda pessoa: '))
p3 = str(input('digite o nome da terceira pessoa: '))
misturar = [p1, p2, p3]
shuffle(misturar)
print('A ordem de agora ficou o seguite:\n'
      '{}'.format(misturar))
