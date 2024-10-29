# Hangman game
#
"""
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.

All functions return something. If a function you write does not return anything (and just prints something to the console), then the default action in Python is to return None.
"""



# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/home/riley/6.0001/edX/UNIT_3/problem set 3/words.txt"

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
    print(len(wordlist), "words loaded.")
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

# test chooseWord
# print(chooseWord(wordlist))

a = chooseWord(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''

    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_ '

    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        letters.remove(letter)

    return ''.join(letters)
    

def hangman(secretWord):
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
    # Initializations
    mistakesMade = 0
    lettersGuessed = []
    maxGuesses = 8
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    # Game loop
    while mistakesMade < maxGuesses:
        print("-------------")
        print("You have", maxGuesses - mistakesMade, "guesses left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters:", availableLetters)
        
        guess = input("Please guess a letter: ").lower()
        
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            mistakesMade += 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        
        # Check if the word is fully guessed
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            return

    # If the loop ends, it means the player lost
    print("-------------")
    print("Sorry, you ran out of guesses. The word was", secretWord + ".")

