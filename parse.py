#use "python parse.py" followed by any words or letters you want a word to contain
# if looking for full words for example "python parse.py strike"
# if looking for parts of words, "python parse.py st ike" 
# you can set a length you want the words to be, add a number anywhere in your command
import sys 
import argparse
if __name__ == "__main__":
    def arraySortedOrNot(arr): #yoinked this bad boy off the internet  
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
            args.append(x) # add non-int arg list

    wordsFile = open("words.txt","r") 
    words = wordsFile.read().splitlines() #set words to a list, each entry is separated by a line break
    for word in words: #for every word
        goodWord = True #resets the flag on each new word check    
        for arg in args: #for every argument
            if word.find(arg) != -1: #if the arg is found in the word
                indicies.append(word.find(arg)) #push the starting index to the indicies array
            if arg not in word: #if the word doesnt contain the argument
                goodWord = False #do not print the word
            if not arraySortedOrNot(indicies): # if the args were not found in order, their starting indicies were not in order
                goodWord = False #dont print
        indicies = []  #clear the array
        if goodWord and maxLength == 0: #if no length was given in the command line
            print(word)
        elif goodWord and maxLength > 0 and len(word) == maxLength: #if a length was given in the command line, print only words of that length
            print(word)
    wordsFile.close()