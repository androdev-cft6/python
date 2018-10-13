# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 03:52:57 2018

@author: andrew
"""

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

import string    # to get ascii letters
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

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))


#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'w', 'l', '', 's', 'a', 'p']
#print(getGuessedWord(secretWord, lettersGuessed))