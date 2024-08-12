def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def obstacle():
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    if at_goal():
        done()
        
    elif not wall_on_right():
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    else:
        turn_left()
    
while at_goal() == False:
    if wall_in_front():
        if right_is_clear():
            turn_right()
        else:
            turn_left()
            obstacle()
    else:
        move()
        
    
        
      
             