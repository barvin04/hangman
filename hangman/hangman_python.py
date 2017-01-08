#hangman
#abhinaba bala "barvin04"    8.1.17
import random #randomly choose words from the array

def my_line():                    ###########print a line
    for s in range(80):
            print ("_", end='')
            
#taking input, appending data so previous data is saved
fhand = open('hangman_data.txt', 'a')             #data in the data-base
while True:
    word = str(input("enter a string : "))
   # word=word+'\n'
    fhand.write(word+'\n')
    q = str(input("to end inputing enter N"))
    if (q ==('N') or q==('n')):                   ##THINK why is it behaving odd
               fhand.close()
               break

#read from the file
inphand = open('hangman_data.txt', 'r')
input_mine = inphand.readlines()       #list of words in the data-base
#print (input_mine)  #::: required during bug searching             
inp_len = len(input_mine)        #number of words
index = random.randint(0,(inp_len-1))
#print ("the randomly generated index is", index) # ::: again, for debugging
word = input_mine[index]
word= word.strip('\n')
leng = len(word)
#print (word, leng)   # ::: for debugging

               ## ______MAIN______##
my_line()
my_line()
e_lst = []
for s in range(leng):
    e_lst.append('_')      
print (e_lst)        #showing the structure
count=1

while True:
    org_lst = list(word)   #doing it again, earlier it was leng
    ask = str(input("enter the letter you bet on:  "))
    if (ask in word):
        for s in range(leng):
            if (org_lst[s]==ask):       #is the character in the word
                e_lst[s]=ask              #find and replace empty with the char          
        print ("good work ... ")
        print (e_lst)
    else:
        print ("sorry, the character is not in the word...Try again!!")
        
    if ('_' not in e_lst):
        my_line()
        my_line()
        print ("CONGO....word sucessfully found")
        print ("it took you ",count,"chances")
        break
    count +=1
    my_line()#35



