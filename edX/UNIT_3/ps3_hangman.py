# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/home/riley/6.0001/edX/UNIT_3/words.txt"

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

    * If the user guesses a letter not in available letters, print
      a message telling the user that they have already guessed that
      letter and need to try again.
    

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    lettersGuessed = []
    mistakesMade = 0
    guessesRemaining = 8
    substring = ''


    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    
    # while the word is not guessed
    while isWordGuessed(secretWord, lettersGuessed) == False:
        print('-------------')
        print('You have', guessesRemaining, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = str(input('Please guess a letter: '))
        
        if guessesRemaining <= 1:
            print('Sorry! That is not in the word. The word was:', secretWord)
            break

        ###
        # if guess is in 'secretWord' and has not been guessed
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            # do not change guessesRemaining

        # if guess not in 'secretWord' and has not been guessed
        elif guess not in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in the word.', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1

        elif guess in secretWord and guess in lettersGuessed:
            # do not change lettersGuessed
            print('Oops! You already guessed that letter (in the word).', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1
        
        elif guess not in secretWord and guess in lettersGuessed:
            print('Oops! You already guessed that letter (not in the word).', getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1

    if isWordGuessed(secretWord, lettersGuessed) == True:
      print('Congratulations, you won!', getGuessedWord(secretWord, lettersGuessed))

        
                
                



# secretWord = chooseWord(wordlist).lower()
secretWord = chooseWord(wordlist)
hangman('testing')