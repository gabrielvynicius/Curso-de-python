maior_peso = 0
menor_peso = float('inf')

for pess in range (1,6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))
    if peso > maior_peso:
        maior_peso =  peso
    if peso < menor_peso:
        menor_peso = peso 

print (f'''O maior peso foi de {maior_peso}Kg 
E a o menor peso e de {menor_peso}Kg''')
