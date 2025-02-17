#desenvolvendo um contador regressivo de fogos de artifício

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOOW!')

#outra forma de fazer
'''from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOOW!')'''

