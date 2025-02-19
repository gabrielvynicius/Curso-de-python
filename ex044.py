#elaborando programa que calcula o valor a ser pago por um produto considerando o preço normal e a condição de pagamento

print('=='*20)
print('Calculando o valor a ser pago por um produto')
print('=='*20)
preco = float(input('Digite o valor do produto: '))
print('=='*20)
print('Qual a forma de pagamento?')
print('=='*20)
print('[1] A vista dinheiro/cheque\n'
      '[2] A vista no cartão\n'
      '[3] 2x no cartão\n'
      '[4] 3x ou mais no cartão')
print('=='*20)
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print(f'O valor a ser pago pelo produto é de R${preco - (preco * 10/100):.2f}')
elif opcao == 2:
    print(f'O valor a ser pago pelo produto é de R${preco - (preco * 5/100):.2f}')
elif opcao == 3:
    print(f'O valor a ser pago pelo produto é de R${preco:.2f}')
elif opcao == 4:
    vezes = int(input('Digite a quantidade de parcelas: ')) #aqui o usuário informa a quantidade de parcelas
    valor = (preco + (preco * 20/100)) / vezes  #aqui é calculado o valor da parcela
    print(f'Sua compra será parcelada em {vezes}x de R${valor:.2f} com juros.') #aqui é calculado o valor da parcela
    print(f'O valor a ser pago pelo produto é de R${preco + (preco * 20/100):.2f}')
print('=='*20)

# End
# By Gabriel Vynicius

# Analysis
# This program calculates the value to be paid for a product considering the normal price and the payment method.
