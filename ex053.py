'''frase = str(input('Digite uma frase: ')).upper().replace(' ','').strip()
frase2 = frase[::-1]
 
print(f'O inverso da frase {frase} corresponde a {frase2}')
if frase == frase2:
    print('Temos um palindromo')
else:
    print('Temos uma frase normal')'''


# A cima está a minha resposta e agora vamos para a do professor

frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')
inverso = ''


for letra in range(len(frase)-1,-1,-1):
    inverso += frase [letra]
    
print(f'O inverso da frase {frase} e {inverso}')
if inverso == frase:
    print('Temos um palindromo.')
else:
    print('A frase não e um palindromo.')