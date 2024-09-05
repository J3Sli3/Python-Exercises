import random 
import Art

def draw_card():
    king = 10
    queen = 10
    jack = 10
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, king, queen, jack,]

    draw = random.choice(cards)
    return draw

def scores(deck : list) -> int:
    if 11 in deck:
        if sum(deck) > 21:
            deck.remove(11)
            deck.append(1)
    score = sum(deck)
    return score

def result(player : int, computer : int) -> str:

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
        play = input("Do you want to play game of Blackjack? Type 'y' or 'n': ").lower()

        if play == "n":
            proceed = False
            break

        elif play == "y":
            print("\n" * 100)
            print(Art.art)
            player = [draw_card(), draw_card()]
            player_current = scores(player)
            
            computer = [draw_card(), draw_card()]
            computer_current = scores(computer)
            
            print(f"Your cards: {player}, current score: {player_current} ")
            print(f"Computer's first card: {computer[0]}")

            while computer_current < 17:
                new = draw_card()
                computer.append(new)
                computer_current = scores(computer)
                
            not_stop = True
            while not_stop == True:
                if player_current > 21 or computer_current > 21:
                    not_stop = False
                
                else:
                    card_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if card_again == "y":
                        new = draw_card()
                        player.append(new)
                        player_current = scores(player)
                        print(f"Your cards: {player}, current score: {player_current} ")
                        print(f"Computer's first card: {computer[0]}")

                        if player_current > 21:
                            break

                    elif card_again == "n":
                        not_stop = False
                        break
                    
            print(f"Your final hand: {player}, current score: {player_current} ")
            print(f"Computer's final hand: {computer}, final score: {computer_current}")
            print(result(player_current, computer_current))


blackjack()
                


                



           
                        




    
 

    
