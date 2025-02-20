from datetime import datetime

ano_atual = datetime.now().year

soma = 0
soma2 = 0
for pessoas in range(1,8):
    num_pessoa = int(input(f'Em que ano a {pessoas}ª nasceu? '))
    if ano_atual - num_pessoa >= 18:
        soma += 1
    else:
        soma2 += 1
print(f'''Ao todo tivemos {soma} pessoas Maior de idade 
E tambem tivemos {soma2} pessoas menores de idade.''')

# By Gabriel Vynicius