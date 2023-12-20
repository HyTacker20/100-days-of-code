import turtle

import pandas

FONT = ("monaco", 12, "bold")

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.bgpic(image)

writer = turtle.Turtle()
writer.up()
writer.hideturtle()

guessed_states = pandas.Series("state")

data = pandas.read_csv("50_states.csv")
states = data["state"]

while len(guessed_states) < 50:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's another state's name?")
    answer = answer_text.title()
    if answer == 'Exit':
        unguessed_states = states[~states.isin(guessed_states)]
        unguessed_states.to_csv("unguessed_states.csv")
        break
    if answer in states.to_list():
        state = data[data["state"] == answer]
        x, y = state.x.item(), state.y.item()
        writer.goto(x, y)
        writer.write(answer, font=FONT, align="center")
        guessed_states = pandas.concat([guessed_states, state.state], ignore_index=True)


screen.exitonclick()
