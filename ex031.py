km = int(input('Qual e a distancia em Km para onde pretende ir? '))
if km <= 200:
    print(f'O valor da sua pasagem vai ser R$ {km * 0.50}')
else:
    print(f'Sua vigem vai custar R$ {km * 0.45}')