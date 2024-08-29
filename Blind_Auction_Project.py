print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''' ) # I could create a different module for the artwork here!
auctions = {} #Create the auction dictionary
def blind_auction():
    proceed = True
    while proceed == True:
        print("Welcome to the Blind Auction Simulator !")   
        name = input("What is your name?: ")     #Prompts users to input their names
        bid = int(input("What is your bid?: $ ")) #Prompts users to input their bids
        auctions[name] = bid   #Adds within the auctions dictionary the names as keys and the bids as values.
        again = input("Are there any other bidders? Type 'yes' or 'no' . \n").lower()  
        if again == "no":
            proceed = False
            maxs = 0
            max_bidder = "nobody"
            for name in auctions:
                if auctions[name] > maxs:  #Finds the largest bid in the dictionary
                    maxs = auctions[name]  #Finds the name associated to the largest bid in the dictionary
                    max_bidder = name
                
                    continue
    
            print(f"The winner is {max_bidder} with a bid of ${maxs}")  #Prints the bidder with the highest bid!
            print("\n" * 2)
            
    
        elif again == "yes":
            print("\n" * 100)  #"Refreshes" the page so that new bidders can't see previous bids!

        else:
            print("\n" * 100)
                
blind_auction()
