print('=' * 40)
print('Vamos pintar uma parede?\n'
      'Para podermos pintar a parede vamos precisar de algumas informações.')
lar = float(input('Quantos metros de largura tem a parede? '))
alt = float(input('Quantos metros de altura tem a parede? '))
area = lar * alt
pint = area / 2
print('Sabendo que a larguara da parede e {} e a altura e {}\n'
      'A area e equivalente a {}M²\n'
      'A quantidade de tinta necessaria para pintar a parede e equivalente a {:.2} Litros.'.format(lar,alt,area,pint))
