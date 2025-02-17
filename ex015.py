print('=' * 100)
n1 = float(input('Quantos Km o carrinho lindo rodou na sua mâo, filho de Deus: Km '))
n2 = int(input('Quantos dias você passou com o HB20 que parece um I30? seria: '))
pn1 = n1 * 0.15
pn2 = n2 * 60
print('Cara não tenho como fazer promoção mas se pagar avista ganha 15% de desconto\n'
      'O total a se pago por diaria ficaria: R$ {}\n'
      'O total a ser pago por Km ficaria: R${}\n'
      'NO final tudo ficaria R$ {} e com desconto ficaria R$ {}, eai vai ser no pix?'
      .format(pn2, pn1, pn1 + pn2, (pn1 + pn2) - ((pn1 + pn2) * 0.15)))
print('=' * 100)
