#take command line args
#put in arr
#loop thru text file
#check if word contains each of the args
import argparse
import sys
if __name__ == "__main__":
    args = []
    goodWord = false
    for x in (sys.argv[1:]):
        args.append(x)
    wordsFile = open("words.txt","r")
    words = wordsFile.read().splitlines()
    for word in words:
        for arg in args:
            if arg not in word:
            
    wordsFile.close()