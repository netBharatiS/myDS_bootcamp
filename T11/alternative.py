
########################################
#In a string make each alternate character to uppercase and
#each other character to lowercase
########################################
sentence = "Hello World"     
new_sentence = " "

for i in range(len(sentence)):                       #for each character of senternce 'Hello World'
    if i % 2 == 0:                                   #for each even indexed characher change to upper
        new_sentence += sentence[i].upper()
    else:                                            #for each odd indexed character change to lower
        new_sentence += sentence[i].lower()
  
    i += 1                          

print(new_sentence)                                 #shold print 'HeLlO WoRlD'  
  
########################################
#In a string make each alternate world to uppercase and
#each other word to lowercase
########################################

sentence1 = "I am learning to code"
new_sentence2 = sentence1.split()                     #split sentence into each words delimited by space and save in list
new_sentence3 = []
i = 0

print(new_sentence2)

for i in range(len(new_sentence2)):                                   #looping on list for each word of the original sentence
    if i % 2 == 0:                                                    #change every even indexed word to lower
        new_sentence3.append(new_sentence2[i].lower())                #change every odd indexed word to upper
    else:
        new_sentence3.append(new_sentence2[i].upper())
    i += 1

print(new_sentence3)                                                  # print new list with changes 
print(" ".join(new_sentence3))                                        # join all items of the list into sentence by using .join() and print
    