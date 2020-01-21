#use "python parse.py" followed by any words or letters you want a word to contain
# if looking for full words for example "python parse.py strike"
# if looking for parts of words, "python parse.py st ike" 
import sys 
import argparse
if __name__ == "__main__":
    args = [] #for storing arguments
    goodWord = True #flag for later
    for x in (sys.argv[1:]): #loop thru args, ignoring the first, which is the script name
        args.append(x) # add to arg list
    wordsFile = open("words.txt","r") 
    words = wordsFile.read().splitlines() #set words to a list, each entry is separated by a line break
    for word in words: #for every word
        goodWord = True #resets the flag on each new word check    
        for arg in args: #for every argument
            if arg not in word: #if the word doesnt contain the argument
                goodWord = False #do not print the word
                
        if goodWord:        
            print(word)
    wordsFile.close()

     #if all(c in word for c in args):
