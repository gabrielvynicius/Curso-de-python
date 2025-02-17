preco = float(input('Digite o preço da ultima coisa que você comprou: R$ '))
desconto1 = preco - (preco * 0.05)
desconto2 = preco - (preco * 0.10)
desconto3 = preco - (preco * 0.20)
desconto4 = preco - (preco * 0.30)
desconto5 = preco - (preco * 0.40)
desconto6 = preco - (preco * 0.5)
print('=' * 50)
print('{} com 5% de desconto ficaria com {}\n'
      'então você vacilou em não pedir desconto.\n'
      'R$ {:.2f} com 10%\n'
      'R$ {:.2f} com 20%\n'
      'R$ {:.2f} com 30%\n'
      'R$ {:.2f} com 40%\n'
      'R$ {:.2f} com 50%'.format(preco, desconto1, desconto2, desconto3, desconto4, desconto5, desconto6))
print('=' * 50)
