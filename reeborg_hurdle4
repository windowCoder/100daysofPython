# SOLVED!!!
def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def jump():
    while not is_facing_north():
        turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()

    
    
while not at_goal():
    if wall_in_front():
        jump()   
    else:
        while not front_is_clear():
            turn_left()
        else:
            move()
        
