import random

play = 0

while play <= 0 :
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    pick = input("")
    
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    
    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    
    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    
    choices = [rock, paper, scissors]
    if pick in ["0","1","2"]:
        if pick == "0":
            print(choices[0])
        elif pick == "1":
            print(choices[1])
        elif pick == "2":
            print(choices[2])
            
            
        computer = random.randint(0,2)
        
        print("Computer chose:")
        print("")
        print("")
        print(f"{choices[computer]}")
        
        if (pick == "0") and (str(computer) == "1"):
            print("You lose")
            
        elif (pick == "0") and (str(computer) == "2"):
                print("You Win")
            
        elif (pick == "1") and (str(computer) == "0"):
                print("You Win")
                
        elif (pick == "1") and (str(computer) == "2"):
                print("You Lose") 
                
        elif (pick == "2") and (str(computer) == "0"):
                print("You Lose")
                
        elif (pick == "2") and (str(computer) == "1"):
                print("You Win")
                
        elif pick == str(computer):
            print("It's a draw")
            
    else:
        print("You typed an invalid number, you lose!")    
            
            
            
        
        
            
            
        
