# Problem Set 2, hangman.py
# Name: Riley Rockwell
# Collaborators:
# Time spent: ~6 hours (multiple sessions)

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/workspaces/6.0001/OCW/problem set 2/words.txt"


def load_words():
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

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
      if letter in letters_guessed:
        return True
    return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return_string = ''

    for letter in secret_word:
        if letter in letters_guessed:
            return_string += letter
        else:
            return_string += '_ '
    
    return return_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string.ascii_letter - letters_guessed
    '''
    alphabet = string.ascii_lowercase
    return ''.join([letter for letter in alphabet if letter not in letters_guessed])


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initialize variables
    guesses_left = 6
    letters_guessed = []
    available_letters = string.ascii_lowercase
    
    # Welcome message and start game
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("-------------")
    
    # Main game loop
    while guesses_left > 0:
        # Display remaining guesses and available letters
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        # Get user input (ensure it's a valid alphabetical character)
        guess = input("Please guess a letter: ").lower()
        
        if guess not in available_letters or guess in letters_guessed:
            print("Oops! You've already guessed that letter or it is invalid. Try again.")
            print("-------------")
            continue

        # Add guess to the list of guessed letters
        letters_guessed.append(guess)

        # Provide feedback based on the guess
        if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            guesses_left -= 1
        
        # Check if the user has guessed the word
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print("-------------")
            print("Congratulations, you won!")
            return
        
        # Display game status
        print("-------------")
    
    # If the user runs out of guesses, end the game
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    cleaned_my_word = my_word.replace(" ", "")
    if len(cleaned_my_word) != len(other_word):
      return False

    for my_char, other_char in zip(cleaned_my_word, other_word):
      if my_char != "_" and my_char != other_char:
        return False
      if my_char == "_" and other_char in cleaned_my_word:
        return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
      print("Possible word matches are:")
      print(" ".join(matches))
    else:
      print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initialize variables
    guesses_left = 6
    letters_guessed = []
    
    # Welcome message and start game
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("-------------")
    
    # Main game loop
    while guesses_left > 0:
      # Display remaining guesses and available letters
      print(f"You have {guesses_left} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      
      # Get user input (ensure it's a valid alphabetical character or *)
      guess = input("Please guess a letter: ").lower()
      
      if guess == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print("-------------")
        continue
      
      if not guess.isalpha() or guess in letters_guessed:
        print("Oops! You've already guessed that letter or it is invalid. Try again.")
        print("-------------")
        continue

      # Add guess to the list of guessed letters
      letters_guessed.append(guess)

      # Provide feedback based on the guess
      if guess in secret_word:
        print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
      else:
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
        guesses_left -= 1
      
      # Check if the user has guessed the word
      if get_guessed_word(secret_word, letters_guessed) == secret_word:
        print("-------------")
        print("Congratulations, you won!")
        return
      
      # Display game status
      print("-------------")
    
    # If the user runs out of guesses, end the game
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

    
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)

    ### hangman w/out hints ###
    # hangman(secret_word)

    ### hangman w/ hints ###
    hangman_with_hints(secret_word)
