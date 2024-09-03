#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")


#here we set the Sairam. You can select any word to play with. 
word = ("Computation")

#creates an variable with an empty value
guesses = ''

#determine the number of Chances
Chances = 10

# Create a while loop

#check if the Chances are more than zero
while Chances > 0:         
    # If yes,
    # make a counter that starts with zero
    failed = 0             

    # checking every character in gussing_word    
    for char in word:      

    # if the character is in the players guess, then
        if char in guesses:    
    
        # print then out the character
            print (char,end=""),    

        else:
    
        # if not found, print a dash
            print ("_",end=""),     
       
        # and increase the failed count with count + one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You Guessed Correct!")
        break            
    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # Chances decreases with count 1 
        Chances -= 1        
 
    # print wrong
        print ("Wrong Guess")  
 
    # how many Chances are left
        print ("You have", + Chances, 'more guesses' )
 
    # if the Chances are equal to zero
        if Chances == 0:           
    
        # print "You Lose"
            print ("You Lose the Game!!!!")
