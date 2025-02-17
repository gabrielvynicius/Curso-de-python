nome = str(input('Digite um nome completo: ')).strip()
print('É {} se disser que esse {} tem ''Silva'' no nome.'.format('silva' in nome.lower(), nome))
