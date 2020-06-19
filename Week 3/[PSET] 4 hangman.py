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
    # FILL IN YOUR CODE HERE...

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-----------')
    lettersGuessed = []
    guesses = 8
    availableLets = getAvailableLetters(lettersGuessed)
    game = isWordGuessed(secretWord, lettersGuessed)
    while guesses >= 1:
      guessedWord = getGuessedWord(secretWord, lettersGuessed)
      
      game = isWordGuessed(secretWord, lettersGuessed)
      print('You have ' + str(guesses) + ' guesses left')
      print('Available letters: ' + availableLets)
      userGuess = input('Please guess a letter: ')
      
      if (userGuess in lettersGuessed):
        print("Oops! You've already guessed that letter: " + guessedWord)
        
      elif (userGuess in secretWord) == False:
        print("Oops! That letter is not in my word: " + guessedWord)
        if (userGuess in availableLets):
          availableLets = availableLets.replace(userGuess, '')
        guesses -= 1
        lettersGuessed += userGuess

      else:
        lettersGuessed.extend(userGuess)
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        availableLets = availableLets.replace(userGuess, '')
        print('Good Guess:' + str(guessedWord))
      print('-----------')
      game = isWordGuessed(secretWord, lettersGuessed)
      if(game == True):
        break
    
    if game:
      print('Congratulations, you won!')
    else:
      print("Sorry, you ran out of guesses. The word was " + secretWord)
    return
