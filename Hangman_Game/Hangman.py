import random

steps = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']

from Words import words

guess = random.choice(words)


lives = 6

hidden = "-" * len(guess)

print(''''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  ''')

print(f"Word to guess: {hidden}")

guesses = set()

lst = []

while lives > 0:
    
    display = ""
    
    tries = input("Guess a letter: ")
    
    guesses.add(tries)
    
    print(f"Letters Guessed: {guesses}")
    
    for i in guess:
        
        
        if i == tries:
            
            display += tries
            
            lst.append(tries)
            
            
            
        elif i in lst:
            
            display += i
            
            
        else:
            
            display += "-"
            
    print(f"Word to Guess : {display}")
            
            
    if "-" not in display:
        print(display)
        print("****************************You Win!****************************")
        break
    
    elif tries not in guess:
        
        lives -= 1
    
        if lives == 0:
            
            if lives == 0:
                
                print(steps[0])            
            
            
            print(f"****************************IT WAS '{guess}'! YOU LOSE!****************************")
            
            break  
              
        
        
        
        elif lives > 0:
            
            if lives == 5:
                
                print(steps[5])
                
            if lives == 4:
                
                print(steps[4])
                
            if lives == 3:
                
                print(steps[3])
                
            if lives == 2:
                
                print(steps[2])
                
                
            if lives == 1:
                
                print(steps[1])
    
            
            
            print(f"You guessed '{tries}', that's not in the word. You lose a life.")
            
            print(f"*****************************{lives}/6 LIVES")

        
    
            
            

        
            
            
            
            
                        
                                                        
                            
                    
              
        
        
                
                
        
                        
                       
                            
                              
                        
                
                
                
                
            
            
            
        
        
