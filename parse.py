#use "python parse.py" followed by any words or letters you want a word to contain
# if looking for full words for example "python parse.py strike"
# if looking for parts of words, "python parse.py st ike" 
import sys 
import argparse
if __name__ == "__main__":
    def arraySortedOrNot(arr):   
        # Calculating length 
        n = len(arr) 
        # Array has one or no element or the 
        # rest are already checked and approved. 
        if n == 1 or n == 0: 
            return True     
        # Recursion applied till last element 
        return arr[0]<= arr[1] and arraySortedOrNot(arr[1:]) 

    #parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='Sets the max number of letters it can have')
    args = [] #for storing arguments
    indicies = [] #storing what index the string checker is at
    maxLength = 0
    goodWord = True #flag for later
    for x in (sys.argv[1:]): #loop thru args, ignoring the first, which is the script name
        if x.isnumeric():
            maxLength = int(x)
        else:
            args.append(x) # add to arg list

    wordsFile = open("words.txt","r") 
    words = wordsFile.read().splitlines() #set words to a list, each entry is separated by a line break
    for word in words: #for every word
        goodWord = True #resets the flag on each new word check    
        for arg in args: #for every argument
            if word.find(arg) != -1:
                indicies.append(word.find(arg))
            if arg not in word: #if the word doesnt contain the argument
                goodWord = False #do not print the word
            if not arraySortedOrNot(indicies):
                goodWord = False
        indicies = []  #clear the array
        if goodWord and maxLength == 0:
            print(word)
        elif goodWord and maxLength > 0 and len(word) == maxLength: 
            print(word)
    wordsFile.close()

     #if all(c in word for c in args):
    # get index of where arg starts, when checking if agr is in word, AND index of arg is greater than all previous args