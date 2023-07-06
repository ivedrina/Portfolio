import random

while True:
    try:
        q= str(input('''Input S -for single player or  
      M- formultiplayer: ''')).lower()  
    except ValueError:
        continue
    if q =='s' or q== 'm':
        break

words=['Action','Address','Affair','Airport','Alcohol','Animal','Answer','Apartment','Apple','Army','Aunt','Awareness']


if q=='s':
    
    word=word_s
    num_ch = set(word)#num of unique ch in string
    n=len(num_ch)
    print('Guess the word:   ' + len(word)*'_ ')
if q=='m':
    word_m=input('Player 1: Type in word: ')
    print(100*'\n')
    word=word_m
    num_ch = set(word)
    n=len(num_ch)
    print('Player 2: Guess the word:   ' + len(word)*'_ ')

k=int(n*1.5)
#print(n)  
#print(word)    
list_guess=[]
c=0
i=0


while i<k:
    guess=input('Choose a letter:  ')
    list_guess.append(guess)
    result = all(elem in list_guess for elem in word)
    if result==True:
        break
    for char in word:    
        if char in list_guess:
            print(char,end =" ")
        else:
            print('_ ',end =" ")
           
    i=i+1
    print('\n')
    #print(list_guess)

for char in list_guess:
    if(word.find(char)!=-1):
        c+=1
# print(c)  
#print(type(list_guess))
if c<n:
    print ('You lost, the word is: ' + word)
else:
    print ('You win')