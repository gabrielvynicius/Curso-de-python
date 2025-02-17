cidade = str(input('Digite um nome de alguma cidade que você conheça: ')).strip()
print('É {} se disser que essa cidade começa com ''Santo''.'. format(cidade[:5].lower() == 'santo'))
