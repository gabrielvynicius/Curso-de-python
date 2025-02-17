from datetime import date
ano = int(input('Digite um ano para verificar se o mesmo e bissexto: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print(f'O ano de {ano} e um ano BISSEXTO.')
else:
    print(f'O ano de {ano} NÃO e um ano BISSEXTO.')