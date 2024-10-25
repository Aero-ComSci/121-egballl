#-----import statements-----
import turtle as t
import random as rand

#-----game configuration----
spotcolor = "purple"
sizes = [2, 1.5, 1, 0.75, 0.5] 
colors = ["red", "green", "blue", "orange", "yellow", "purple"] 
shape = "triangle"
score = 0
fontsetup = ("Arial", 20, "normal")

timer = 5
counter_interval = 1000 
timer_up = False

#-----initialize turtles-----
scorewriter = t.Turtle()
counter = t.Turtle()
game_turtle = t.Turtle()
scorewriter.penup()
scorewriter.hideturtle()
scorewriter.goto(200, 200)  
counter.penup()
counter.hideturtle()
counter.goto(-200, 200) 


game_turtle.shape(shape)
game_turtle.fillcolor(spotcolor)

#-----game functions--------
def tclicked(x, y):
    if not timer_up: 
        stamp()
        change_position()
        change_size()
        updatescore()

def change_position():
    new_xpos = rand.randint(-250, 250)
    new_ypos = rand.randint(-250, 150)
    game_turtle.penup()
    game_turtle.goto(new_xpos, new_ypos)

def updatescore():
    global score
    score += 1
    scorewriter.clear()
    scorewriter.write(f"Score: {score}", font=fontsetup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=fontsetup)
        timer_up = True
        game_turtle.hideturtle()  
    else:
        counter.write(f"Timer: {timer}", font=fontsetup)
        timer -= 1
        t.ontimer(countdown, counter_interval)

def stamp():
    game_turtle.color(rand.choice(colors))  
    game_turtle.stamp()  
    game_turtle.color(spotcolor)  

def change_size():
    new_size = rand.choice(sizes)
    game_turtle.shapesize(new_size)

def start_game():
    global timer, score, timer_up
    timer = 5  
    score = 0  
    timer_up = False
    game_turtle.showturtle()  
    updatescore()
    countdown()

#-----events----------------
game_turtle.onclick(tclicked)
start_game() 

#-----screen setup-----------
wn = t.Screen()
wn.bgcolor("lightblue")  
wn.mainloop()
