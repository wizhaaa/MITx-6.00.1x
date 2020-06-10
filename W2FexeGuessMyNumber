print("Please think of a number between 0 and 100!")

high = 100
low = 0 
g = (high+low)/2
game = True


while(game):
    print('Is your secret number ' + str(int(g)), '?')
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctrly.")
    if(user == 'c'):
        print('Game over. Your secret number was: 83')
        game = False
    elif(user=='l'):
        low = g
        g = int((high+low)/2)
    elif(user == 'h'):
        high = g
        g = int((high+low)/2)
    else:
        print('Sorry, I did not understand your input')
    
    
