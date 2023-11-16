# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def in_field():
    if front_is_clear() and right_is_clear():
        turn_left()
        turn_left()
        if front_is_clear() and right_is_clear():
            turn_left()
            turn_left()
            return True
        turn_left()
        turn_left()
    return False


while not at_goal():
    if in_field():
        move()
        if front_is_clear():
            move()
    if right_is_clear():
        turn_right()
    elif front_is_clear() and wall_on_right():
        move()
    else:
        turn_left()
    if front_is_clear():
        move()
done()
