from turtle import *
import turtle 
import random 
import time 
 
width = height = 500 
win = turtle.Screen() 
win.setup(width, height) 
win.bgcolor("sky blue") 
win.title("Pythontpoint") 
 
sb_rate = 1, 3 
sb_size = 5, 15 
wind_change = 1, 5 
max_wind = 3 
 
 
def make_circle(turtle_name, x, y, size, colour): 
    turtle_name.color(colour) 
    turtle_name.penup() 
    turtle_name.setposition(x, y) 
    turtle_name.dot(size) 
 

list_of_sbs = [] 
def make_sb(): 
    sb = turtle.Turtle() 
    sb.color("white") 
    sb.penup() 
    sb.setposition(random.randint(-2*width, width/2), height/2) 
    sb.hideturtle() 
    sb.size = random.randint(*sb_size) 
    list_of_sbs.append(sb) 
 
def move_sb(turtle_name, falling_speed=1, wind=0): 
    turtle_name.clear() 
    turtle_name.sety(turtle_name.ycor() - falling_speed) 
    if wind: 
        turtle_name.setx(turtle_name.xcor() + wind) 
    turtle_name.dot(turtle_name.size) 
 
 
sm = turtle.Turtle() 
x_position = 0 
y_positions = 75, 0, -100 
size = 75 
for y in y_positions: 
    make_circle(sm, x_position, y, size, "white") 
    size = size *1.5 
 
 
button_seperation = 25 
button_y_positions = [y_positions[1]-button_seperation, 
                      y_positions[1], 
                      y_positions[1]+button_seperation] 
for y in button_y_positions: 
    make_circle(sm, x_position, y, 10, "black") 
 
 
y_offset = 10 
x_seperation = 15 
for x in x_position-x_seperation, x_position+x_seperation: 
    make_circle(sm, x, y_positions[0] + y_offset, 20, "green") 
    make_circle(sm, x, y_positions[0] + y_offset, 10, "black") 
 
 
sm.color("orange") 
sm.setposition(x_position - 10, y_positions[0]-y_offset) 
sm.shape("triangle") 
sm.setheading(200) 
sm.turtlesize(0.5, 2.5) 
 
win.tracer(0) 
 

ground = turtle.Turtle() 
ground.fillcolor("forest green") 
ground.penup() 
ground.setposition(-width/2, -height/2) 
ground.begin_fill() 
for _ in range(2): 
    ground.forward(width) 
    ground.left(90) 
    ground.forward(70) 
    ground.left(90) 
ground.end_fill() 
 
ground = turtle.Turtle() 
for x in range(int(-width/2), int(width/2), int(width/200)): 
    make_circle(ground, x, -180, random.randint(5, 20), "white") 
 
txt = turtle.Turtle() 
txt.color("Purple") 
txt.penup() 
txt.setposition(-100,190) 
txt.write("Pythontpoint", font=("purple", 30, "bold"), align="center") 
txt.setposition(130, 150) 
txt.color("green") 
txt.write("Wishing You ", font=("blue", 30, "bold"), align="right") 
txt.color("red")
txt.setx(10)
txt.setposition(90, 110) 
txt.write("Happy New Year", font=("red", 30, "normal"), align="center") 
 
#txt.write("from", font=("Apple Chancery", 20, "bold"), align="right") 
txt.hideturtle() 
 
time_delay = 0 
start_time = time.time() 
wind = 0 
wind_delay = 5 
wind_timer = time.time() 
wind_step = 0.1 
while True: 
    if time.time() - start_time > time_delay: 
        make_sb() 
        start_time = time.time() 
        time_delay = random.randint(*sb_rate)/10 
 
    for sb in list_of_sbs: 
        move_sb(sb, wind=wind) 
        if sb.ycor() < -height/2: 
            sb.clear() 
            list_of_sbs.remove(sb) 
 
    if time.time() - wind_timer > wind_delay: 
        wind += wind_step 
        if wind >= max_wind: 
            wind_step = -wind_step 
        elif wind <= 0: 
            wind_step = abs(wind_step) 
 
        wind_timer = time.time() 
        wind_delay = random.randint(*wind_change)/10 
 
 
    win.update() 
 
turtle.done()