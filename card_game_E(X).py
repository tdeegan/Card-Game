"""This program determines the expected value of a card game in which you randomly draw from a standard deck with the following rules:

   1. Black card is worth $1
   2. Red card is worth -$1
   3. You can quit at any time.

It employes elements of dynamic programming with a recursive solution and allows for the user to input a hypothetical situation in the game."""

import locale
locale.setlocale(locale.LC_ALL,'English_United States.1252')

def memoize(f): #f is exp_value
    memo = {} #dictionary of expected values
    
    def helper(a,b):
        if (a,b) not in memo:
            entry = 0
            sc = a-b #current score
            
            if(sc > f(a,b)): #current score exceeds calculated exp value
                entry = sc #define current score to be expected value
            else:
                entry = f(a,b)
            memo[(a,b)]= entry
        return memo[(a,b)]
    return helper

@memoize
def exp_value(i,j):
    if(i == 0): #only black cards remain, so after selecting them all, cumulative winnings is $0
        return 0
    elif (j == 0): #no more black cards to select, so stop drawing cards.  Current score is i
        return i
    else:
        return (i/(i+j))*exp_value(i-1,j)+(j/(i+j))*exp_value(i,j-1) #recursively solve
            
def func(x,y):#x is cards in hand, y is black cards in hand
    redsInHand = x-y
    blacksInHand = y
    redsRemaining = 26 - redsInHand
    blacksRemaining = 26 - blacksInHand
    currentScore = blacksInHand - redsInHand
    expValue = 0
    
    if(currentScore >= exp_value(redsRemaining,blacksRemaining)):
        expValue = currentScore #define expected value to be current score
    else:
        expValue = exp_value(redsRemaining, blacksRemaining) #use recurrence relation
    
    if(x==0 and y ==0): #game has not yet started
        print('\nThe expected value of the game before drawing the first card is: ',locale.currency(expValue))
        print('Therefore, it makes sense to play and you should begin drawing cards.\n')
        
    elif(currentScore == expValue): #currentScore was greater than or equal to value calculated by recurrence relation
        print('\nCurrent score of: ', locale.currency(currentScore),' is the current expected value of the game.')
        print('Stop drawing cards.')
    else:
        print('\nCurrent score of: ', locale.currency(currentScore),' is less than the current expected value of the game: ',locale.currency(expValue))
        print('Continue drawing cards')
        
def main():

    func(0,0) #determine expected value of the game before any cards are drawn

    marker = '1' #user will select 1 to continue, any other value to quit

    while(marker == '1' or marker == 'Yes' or marker == 'YES' or marker == 'yes' or marker == 'y' or marker == 'Y'): 
        print('\nProvide total number of cards currently in hand and total number of black cards currently in hand.')
    
        try:
            X = int(input('Total cards in hand: '))
        except ValueError:
            print('Value must be an integer')
            continue
    
        while(X > 52 or X < 0):
            X=int(input('Value must be between 0 and 52 inclusive.  Enter total number of cards in hand: '))
        
        try:
            Y = int(input('Black cards in hand: '))
        except ValueError:
            print('Value must be an integer')
            continue
    
        while(Y > 26 or Y < 0 or Y > X or X-Y > 26):
            try:
                Y=int(input('Invalid entry.  Please enter number of black cards in hand: '))
            except ValueError:
                continue
        func(X,Y)
    
        marker = input('\nRun again? [Yes=1, No=0]: ')
    
    print('\nProgram terminated.')

if __name__ == "__main__":
    main()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
