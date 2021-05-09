import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
name_states = data.state.to_list()
print(name_states)
guess_state = []
while len(guess_state) < 50:
    answer_state = screen.textinput(title= f"{len(guess_state)}/50 Guess is Correct",
                                    prompt= "What is another state is name?").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in name_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0, 0)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()