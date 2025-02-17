'''ano = int(input('Digite o ano que você naceu: '))
idade = 2025 - ano
if idade <= 9:
    print(f'Você ainda e Mirin {idade}')
elif 9 < idade <= 14:
    print(f'Você já é infantil {idade}')
elif 14 < idade <=19:
   print(f'Você já e Junior {idade}')
elif 19 < idade <=20:
    print(f'Você ja e Senior {idade}')
else: 
    print(f'Voce ja e Master {idade}')
'''

#analisando o codigo acima, percebemos que ele esta correto, porem podemos melhorar ele, veja abaixo:

from datetime import date
ano  =  int(input('Digite o ano que você naceu: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você ainda e Mirin {idade}')
elif 9 < idade <= 14:
    print(f'Você já é infantil {idade}')
elif 14 < idade <=19:
    print(f'Você já e Junior {idade}')
elif 19 < idade <=20:
    print(f'Você ja e Senior {idade}')
else:
    print(f'Voce ja e Master {idade}')
    
# Perceba que o codigo acima esta mais limpo e mais facil de entender.
# Alem de que, agora ele pega a data atual do sistema, e não precisamos ficar mudando o ano manualmente.
# O metodo date.today().year pega a data atual do sistema.
# E o metodo .year pega somente o ano.
# by: Gabriel Vynicius
