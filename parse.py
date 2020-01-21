#use "python parse.py" followed by any words or letters you want a word to contain
# if looking for full words for example "python parse.py strike"
# if looking for parts of words, "python parse.py st ike" 
import sys 
import argparse
if __name__ == "__main__":
    def check(list1, val): 
        for x in list1: 
            if val <= x: 
                return False 
        return True
      
    args = [] #for storing arguments
    indicies = [] #storing what index the string checker is at
    goodWord = True #flag for later
    for x in (sys.argv[1:]): #loop thru args, ignoring the first, which is the script name
        args.append(x) # add to arg list
    wordsFile = open("words.txt","r") 
    words = wordsFile.read().splitlines() #set words to a list, each entry is separated by a line break
    for word in words: #for every word
        goodWord = True #resets the flag on each new word check    
        for ind, arg in enumerate(args, start=0): #for every argument
            if word.find(arg) != -1:
                indicies.append(word.find(arg))
            if arg not in word and check(indicies, word.find(arg)) : #if the word doesnt contain the argument
                goodWord = False #do not print the word
        indicies = []  #clear the array
        if goodWord:        
            print(word)
    wordsFile.close()

     #if all(c in word for c in args):
    # get index of where arg starts, when checking if agr is in word, AND index of arg is greater than all previous args