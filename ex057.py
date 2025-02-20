'''while True:
    sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()

    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Dados inválidos. por favor informe novamente seu sexo: ') 


if sexo == 'M':
    print('Sexo M registrado com sucesso')
if sexo == 'F':
    print('Sexo F regitrado com sucesso')'''

# Acima esta a minha resolução Abaixo esta a resolução conforme a do professor.

sexo = str(input('Digite seu sexo: [F/M] ')).strip().upper()[0]

while sexo not in  'MF':

    sexo  = str(input('Dados inválidos. por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} Registrado com sucesso. ')

# By Gabriel Vyncicius.