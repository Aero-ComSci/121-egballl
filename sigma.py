# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand

#-----game configuration----
spotcolor = "purple"
size = 2
shape = "triangle"
score = 0
fontsetup = "Arial", 20, "normal"
#-----initialize turtle-----
scorewriter = t.Turtle()
t.shape(shape)
t.shapesize(size)
t.fillcolor(spotcolor)
#-----game functions--------
def tclicked(x, y):
    print("Spot Clicked!")

def change_position(x, y):
    new_xpos = rand.randint(1, 100)
    new_ypos = rand.randint(1, 100)
    t.penup()
    scorewriter.penup()
    t.hideturtle()
    scorewriter.hideturtle()
    t.goto(new_xpos, new_ypos)
    scorewriter.goto(new_xpos, new_ypos)
    t.showturtle()
    scorewriter.showturtle()
    t.pendown()
    scorewriter.pendown()
    updatescore()

def updatescore():
    global score
    score += 1
    scorewriter.clear()
    scorewriter.write(score, font= fontsetup)
    

#-----events----------------
t.onclick(change_position)





wn = t.Screen()
wn.bgcolor("Blue")
wn.mainloop()
