n1 = float(input('Digite um valor em metros: '))
km = n1 /1000
he = n1/100
de = n1/10
c = n1 * 100
m = n1 * 1000
print('{} Metros equivalem á \n'
      '{:0.3f}Km\n'
      '{:0.2f}Hm\n'
      '{:0.1f}dam\n'
      '{}cm\n'
      '{}mm'.format(n1,km,he,de,c,m))
