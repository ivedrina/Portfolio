text=input("Enter text: ")


count_letters=len([ele for ele in text if ele.isalpha()])

count_word = text.count(' ')+1

count_sentences = text.count('.')+text.count('?')+text.count('!')

index = 0.0588 * 100 * count_letters /count_word - 0.296 * 100 * count_sentences /count_word  - 15.8

#print(count_letters)
#print(count_word)
#print(count_sentences)
#print(index)

if index > 1 and index < 16:
   print("Grade " + (str(round(index)) ) )      

if index < 1:
    print("Before Grade 1")

if ( index > 16 ):
    print("Grade 16+")
