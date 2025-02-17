frase = str(input('Digite uma frase: ')).strip().lower()
print('''A letra "A" aparace {} Vezes
A letra "A" aparece pela primeira vez no indice {}
A letra "A" aparece pela ultima vez no indice {}'''
      .format(frase.lower().count('a'),frase.find('a')+1,frase.rfind('a')+1))
