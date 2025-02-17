import random
maquina = (random.randint(1,5))
usuario = int(input('divinhe o numero que estou pensando: '))
if  usuario < maquina:
    print(f'Infelizmente o era um pouco mais, O numero que escolhi foi {maquina}')
elif usuario > maquina:
    print(f'Infelizmente o numero era um pouco mais, O numeor que escolhi foi {maquina}')
else:
    print(f'Parabéns realmente pensei no numero {maquina}')