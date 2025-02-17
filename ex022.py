nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
print('''O nome com letras maiusculas: {}
O nome com letras minusculas: {}
Quantidade de Indices presentes no que foi digitado: {}
Quantidade de letras ao todo sem considerar os espaços: {}
Quantidade de letras que tem o primeiro nome: {}'''
      .format(nome.upper(), nome.lower(), len(nome), len(nome.replace(' ','')),len(dividido[0])))
