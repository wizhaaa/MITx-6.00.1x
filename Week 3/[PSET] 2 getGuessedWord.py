def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    x = len(secretWord)
    new = str('_'*x)
    guessed = list(new)

    for i in range(x):
      if (secretWord[i] in lettersGuessed) == True:
        guessed[i] = secretWord[i]

    display = ' '.join(guessed)

    return(display)
