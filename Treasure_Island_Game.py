print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

direction = input('      Type "left" or "right"      ')
if direction == "right":
    print("You fell into a hole. Game Over.")
    
elif direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    water = input('  Type "wait" to wait for a boat. Type "swim" to swim across. ')
    
    if water == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doors = input("  One red, one yellow and one blue. Which colour do you choose? ")
        
        if doors == "blue":
            print("You enter a room of beasts. Game Over.")
            
        elif doors == "yellow":
            print("")
            print("There is a dragon standing before you!")
            print('''
           """---==____   ____==---"""
        """"---==='__  """  __`===---"""'
         """"--===(___=-_-=___)===--""""
         """"--=== ) _=====_ ( ===--""""
          """"--===//"\"""/"\\===--""""
  ___----______---|___-----___|---______-----___
,'        """"--==`\`       '/'==--""""       __`----__
\          """"---==| \   / |==---""""  __--""  """"-_
 \                  `:-| |-:'      \ /'"              `
  )                 | `/ \' |      /'     ,------_      `
 '                  | `-^-' |    /'     /'        `\      
                    |       |   |     /\\           \      
                    |       |  |     |  \ \          \      
                    \       \  |     |___) )  [pb]   |      |
                    \       \-"|     |_---'          |      |
                    _\       \-\     \              /       |
                  /' \       \  \     \         _,-"       /
                /   _-\       \__\_____\____--""         /
               (   ""--\                               /'
                `-__    \_                         _,-'
                    `--_  "-___________________--""
                        `\   \__    )    )
                          \     "--"    /
                           \__        /'
                              ""---"" ''')
            print("")
            print("")
            print('''Type "spear" to fight the dragon with a Dragon's Bone Spear.''')
            print("")
            print('''Type "sword" to fight the dragon with a Flaming Sword of despair.''')
            print("")
            print('''Type "net" to bind the dragon in an Enchanted Net of Binding! ''')
            print("")
            weapon = input("Which weapon will you pick? ")
            
            if weapon == "spear":
                print("")
                print("With a precise thrust, the spear pierces the dragon's heart.")
                print("The Dragon has been defeated!")
                print("")
                print("You now stand in front of an Ancient Guardian.")
                print('''
                              .sSSSSSSSs
                              sSS=""^^^"s
                  /\       , /  \_\_\|_/_)
                 /';;     /| \\\/.-. .-./
                / \;|    /. \,S'  -   - |
               / -.;|    | '.SS     _|  ;
              ; '-.;\,   |'-.SS\   __  /S
              | _  ';\\.  \' SSS\_____/SS
              |  '- ';\\.  \_SSS[_____]SS
              \ '--.-';;-. __SSS/\    SSS
               \  .--' ';;'.=SSS`\\_\_SSS
                `._ .-'` _';;..=.=.=.\.=
                   ;-._-'  _.;\.=.=.=.|.=|
         ,     _.-'    `"=._  ;\=.=__/__/
         )\ .'`   __        ".;|.=.=.=./
         (_\   .-`  '.   |    \/=.=.=/`
          /\\         \-,|     |.--'|
         /  \`,       //  \    | |  |
        ( (__) )  _.-'--,  \   | |  '--,
         ;----' -'--,__}  \  '--, __}
  jgs    \_________}       \___}
''')
                print("")
                print("He gives you a One-Word answer riddle to answer in order to access the treasure.")
                print("")    
                print("I am not alive, yet I grow; I don't have lungs, yet I need air;")
                print("I don't have a mouth, yet water kills me. What am I?")
                print("")
                answer = input("Input your Answer ")
                
                if answer == "fire":
                    print("You found the treasure! You Win!")
                    print("")
                    print('''         __________
        /\____;;___
       | /         /
       `. ())oo() .
        |\(%()*^^()^
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %''')
                
                else:
                    print("A trap beneath you opens, and you fall to your death. Game Over.")
                    
                
                
                
            elif weapon == "sword":
                print("As the character swings the sword, its fiery blade ignites uncontrollably,") 
                print("engulfing both them and the dragon in a cataclysmic inferno that leaves nothing but ashes! Game Over.")
            elif weapon == "net":
                print("The net ensnares the dragon but fails to hold it;")
                print("the dragon's furious thrashing causes the net to snap back violently,")
                print("crushing the character beneath its tangled remnants. Game Over.")
                
            else:
                print("The Dragon stomps on you, leaving your broken body on the ground")
             
            
        elif doors == "red":
            print("It's a room full of fire. Game Over.")
            
        else:
            print("Game Over.")
            
        
        
    else:
        print("You get attacked by an angry trout. Game Over.")
        
        
else:
    print("You fell into a hole. Game Over.")
    
        
    
    
    
    
   