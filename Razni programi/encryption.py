import sys
import random

text = input('Enter text you wish to encrypt: ')

if len(sys.argv) == 2:
    k=sys.argv[1]
    print('You chose self encryption.')
    #print(k)
else:
   print('You chose computer encryption.')
   k=(str(random.randint(1,15)))
   #print(k)
   with open('key.txt', 'w') as f:
    print('Your encryption key is '+ k +'.', file=f)

for ch in range(0, len(text)):
    if text[ch].isalpha():
        if text[ch].islower() :
            e_text= (ord(text[ch])-97+int(k))%26+97
            print(chr(e_text), end='')
        elif text[ch].isupper():
            e_text= (ord(text[ch])-65+int(k))%26+65
            print(chr(e_text), end='')
    else:
        print(text[ch], end='')
print('\n')


