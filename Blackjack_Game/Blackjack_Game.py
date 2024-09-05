import random 
import Art

def draw_card():
    king = 10
    queen = 10
    jack = 10
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, king, queen, jack,]     #In Blackjack, the king, the queen, and the jack are all worth 10 in Blackjack

    draw = random.choice(cards)
    return draw

def scores(deck : list) -> int:
    if 11 in deck:
        if sum(deck) > 21:                 #Checks if the hand with the 11 Ace is greater than 21; if yes it switches the 11 for 1.
            deck.remove(11)
            deck.append(1)
    score = sum(deck)
    return score

def result(player : int, computer : int) -> str:
    """
    Uses two int parameters, player and computer, and returns whether the computer has won or not.
    """

    if player > computer:
        if player <= 21:
            return "You Win 😃"
        elif player > 21:
            return "You Went Over!. You lose 😭)"
        
    elif computer > player:
        if computer <= 21:
            return "You Lose 😔"
        elif computer > 21:
            return "Opponent went over. You win 😁"
        
    elif player == computer:
        return "It's a draw 😐"
    else:
        return "You Lose"

def blackjack():
    proceed = True
    while proceed == True:
        play = input("Do you want to play game of Blackjack? Type 'y' or 'n': ").lower()  #Keeps on looping to ask if you want to play again until you say ("n")o.

        if play == "n":
            proceed = False
            break

        elif play == "y":
            print("\n" * 100)
            print(Art.art)         #Prints the image from the Art module
            player = [draw_card(), draw_card()]
            player_current = scores(player)
            computer = [draw_card(), draw_card()]
            computer_current = scores(computer)
            #Generates randomly the first two cards for both the player and the computer, and later finds the sum of their hand

            print(f"Your cards: {player}, current score: {player_current} ")
            print(f"Computer's first card: {computer[0]}")

            while computer_current < 17:
                new = draw_card()
                computer.append(new)
                computer_current = scores(computer)
                #Keeps on drawing cards for the computer until it has a hand of 17 or more.
                
            not_stop = True
            while not_stop == True:
                if player_current > 21 or computer_current > 21:
                    not_stop = False
                    #Instantly stops the loop if either the computer or the player has a hand greater than 21
                
                else:
                    card_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if card_again == "y":
                        new = draw_card()
                        player.append(new)
                        player_current = scores(player)
                        print(f"Your cards: {player}, current score: {player_current} ")
                        print(f"Computer's first card: {computer[0]}")
                        #start a loop of asking the player if he wants to draw a card again and if yes, the card is added to the hand.
                        # and the new hand-score is calculated. 

                        if player_current > 21:
                            break
                        #stops the loop if the new score is greater than 21.

                    elif card_again == "n":
                        not_stop = False
                        break
                    #stops the loop if the player does not want to draw a card again.

            print(f"Your final hand: {player}, current score: {player_current} ")
            print(f"Computer's final hand: {computer}, final score: {computer_current}")
            print(result(player_current, computer_current))
            #prints the results for both the computer and the player and calls on the function result to determine
            #who won between the computer and the user.



blackjack()
                


                



           
                        




    
 

    
