import random

def hangman_game():#function definition
    choice='Y'
    while(choice=='Y'):
        print('Guess the letters')
        guess_word=''#variable to store user guessed letter
        list_word=['Developer','Hardware','Software','Tiger','Shape','Coconut','Programming','Color',"Java","DataScience","Machinelearning",'Python','Javascript','Elephant','Hobby','Ointment','Pigeon','Eagle','Anchor','Cabbage','Bread','Computer']#list of words
        actual_word=random.choice(list_word)#function that generate random word
        actual_word=actual_word.lower()#converting actual_word into lowercase
        attempt=10#variable to keep track of number of guesses done by user
        while attempt>0:
            word=''#variable to keep track of letter entered  by user

            #for loop will run till the length  of the    actual word
            for letter in  actual_word:
                
                if letter in guess_word:
                    word=word+letter#if letter is present in guess word then will concatenate the letter variable with word variable.
                        
                else:
                    word=word+ "_ " #number of dashes will be created is equal to the length of the actual_word variable
          
            print(word)
            
            if word==actual_word:
                print('***** Congratulation******')
                print("You won!")
                break   #to come out from the inner while loop
            
            
            user_guess=input("Guess a  letter :")#user is ask to enter the letter
            user_guess=user_guess.lower()
            guess_word=guess_word+user_guess#concatenating the user_guess letter
        
            #if user_guess is not present in actual word will decrease the attempt variable everytime the users enter  the incorrect letter     
            if user_guess not in actual_word:
                attempt=attempt-1
                print('*'*10)
                print("Number of Guesses left:",attempt)
                print('*'*10)
                #if attempt become zero that means the user have not correctly guess the letter.
                if attempt==0:
                    print("Sorry you loss the game!")
                    print("The correct word is",actual_word)
                    break#to come out from the inner while loop
      
        choice=input("Do you want to play  the game again  Y:Continue  N:Exit")
        choice=choice.upper()
        


hangman_game()

        


       

        
