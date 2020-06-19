def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    avail = 'abcdefghijklmnopqrstuvwxyz'
    guessed = set(lettersGuessed)
    avail = { x for x in avail if x not in guessed }
    avail = sorted(avail)
    avail = ''.join(avail)
    return avail
