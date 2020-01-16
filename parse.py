#take command line args
#put in arr
#loop thru text file
#check if word contains each of the args
import argparse

if __name__ == "__main__":
   # int hits = 0
    parser = argparse.ArgumentParser(description="")
    wordsFile = open("words.txt","r")
    words = wordsFile.read()
    print(words)
    wordsFile.close()
    
        