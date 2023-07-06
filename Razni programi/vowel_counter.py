a = input('Input text: ')
s= a.lower()
print (len(s))


count =0    

for i in range(len(s)):
    if s[i] == 'a':
        count = count +1 
    elif s[i] == 'e':
        count = count +1
    elif s[i] == 'i':
        count = count +1
    elif s[i] == 'o':
        count = count +1
    elif s[i] == 'u':
        count = count +1
print ('The number of vowels in the text is ' +str(count))


a = input('Input text: ')
s= a.lower()
print (len(s))


count =0
counta=0
counte=0
counti=0
counto=0
countu=0

for i in range(len(s)):
    if s[i] == 'a':
        counta = counta +1 
    elif s[i] == 'e':
        counte = counte +1
    elif s[i] == 'i':
        counti = counti +1
    elif s[i] == 'o':
        counto = counto +1
    elif s[i] == 'u':
        countu = countu +1
count =  counta + counte+ counti + counto +countu 
print ('The number of vowels in the text is ' +str(count))
print ('E is in text  ' +str(counte) +' times.')
print ('A is in text  ' +str(counta) +' times.')
print ('I is in text  ' +str(counti) +' times.')
print ('O is in text  ' +str(counto) +' times.')
print ('U is in text  ' +str(countu) +' times.')