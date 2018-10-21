# Hangman game
#
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...   
    for ch in secretWord:
        if ch not in lettersGuessed:
            gessed=False
            break
        else:
            gessed=True
    return gessed      

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    strTemp=''
    for ch in secretWord:
        if ch in lettersGuessed:
            strTemp+=ch
        else:
            strTemp+="_ "
    
    return strTemp

import string  # to get ascii letters
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
        # FILL IN YOUR CODE HERE...
    listAllChar=list(string.ascii_lowercase)
    for ch in lettersGuessed:
        if ch in listAllChar:
            listAllChar.remove(ch)
    return ''.join(listAllChar)

    # FILL IN YOUR CODE HERE...
def selectLevel():
    print("There are three difficulty levels, Please choose one")
    level=input("Easy-1 Medium-2 Advanced-3 ==> ")
    return int(level)
    
def hangman(secretWord):
    import winsound
    import time
    from PIL import Image
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...                            
    lettersGuessed=[]
    level=selectLevel()
    
    if level==1:
        MAX_TRIES=30
    elif level==2:
        MAX_TRIES=len(secretWord)*2
    elif level==3:
        MAX_TRIES=len(secretWord)
    else:
        MAX_TRIES=10
    
    mistakesMade=0
    availableLetters=getAvailableLetters(lettersGuessed) 
    guessedWord=getGuessedWord(secretWord, lettersGuessed)
    
    print("Welcome to the game, Hangman!")
    print("I'm thinking of a word that is " + str(len(secretWord)) + 
          " letters long")    

    print(secretWord)
                             
    while not isWordGuessed(secretWord, lettersGuessed):
        print("\n" +"-"*50 + "\n")
        print("You have " + str(MAX_TRIES-mistakesMade) + " guessed left")
        print("Available letters: " + availableLetters)
        print("Your word looks like this: " + guessedWord)
        guessedLetter=input("Please guess a letter -> ").lower()

        while guessedLetter in lettersGuessed:
            print("Oops, you've already guessed this letter " + guessedLetter)
            winsound.MessageBeep(winsound.MB_ICONHAND)
            print("Available letters: " + availableLetters)
            guessedLetter=input("Please guess a letter -> ").lower()                    
        
        lettersGuessed.append(guessedLetter)
        availableLetters=getAvailableLetters(lettersGuessed)
                    
        if guessedLetter in secretWord:
            guessedWord=getGuessedWord(secretWord, lettersGuessed)
            print("Good guess!!!")
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        else:
            mistakesMade+=1
            print("Oops, you guessed wrong.")
            winsound.MessageBeep(winsound.MB_ICONHAND)
                                        
        if mistakesMade>=MAX_TRIES:
            print("\nYou lost. Secret word was: " + secretWord)
            print("Game over!")
            time.sleep(1.5)
            winsound.PlaySound("soundSadtrombone.wav",winsound.SND_ASYNC)  
            Image.open("hangman.jpg").show()
            break
    
    if isWordGuessed(secretWord,lettersGuessed):
        print("You guessed right! -> " + guessedWord)
        print("You won!")
        winsound.PlaySound("soundTaDa.wav",winsound.SND_ASYNC)
        time.sleep(1.5)
        Image.open("fireworks.jpg").show()

# Running the program        
secretWord = chooseWord(wordlist).lower()       
hangman(secretWord)
