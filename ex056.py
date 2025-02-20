
'''media_idade = 0  # Aqui serve para verificar a media de idade do grupo.
h_mais_velho = 0 # Aqui serve para verificar qual e o homem mais velho. 
nome_mais_velho = '' # Aqui serve para verificar o nome do homem mais velho.
m_menor = 0 # Aqui seve para verificar quantas mulheres tem menos d 20 anos.

for p in range(1,5):

    print('-' * 5, f'{p}ª Pessoa','-' * 5)
    nome = str(input('Nome: ')).strip
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    media_idade += idade

    if sexo == 'M' and idade > h_mais_velho:
        h_mais_velho = idade
        nome_mais_velho=nome
    
    if sexo == 'F' and idade <20:
        m_menor += 1

media_idade /= 4  
print()

print(F'A media de idade do grupo é de {media_idade}
O Homem mais velho tem {h_mais_velho} Anos  e se chama {nome_mais_velho}.
Ao todo são {m_menor} Mulheres com menos de 20 anos.)'''


# Acima esta comom eu fiz a resolução do problema abaixo se encontra a resolução do professor.


soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_do_homem_mais_velho = ''
total_de_mulher_menor_20 = 0 

for pessoas in range(1,5):
    print(f'----- {pessoas}ª pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    soma_idade += idade

    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_do_homem_mais_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_do_homem_mais_velho

    if sexo in 'Ff' and idade < 20:
        total_de_mulher_menor_20 += 1

media_idade = soma_idade / 4

print() 

print(f'''A media de idade do grupo é {media_idade},
O home mais velho tem {maior_idade_homem} e seu nome é {nome_do_homem_mais_velho}
Ao todo temos {total_de_mulher_menor_20} Mulheres menores de 20 anos. ''')