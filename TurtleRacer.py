import turtle
import time
import random
WIDTH,HEIGHT=500,500
COLORS=["red",'orange','green','cyan','blue','yellow','black','purple','pink','brown']

def get_turtle_racers():
    racers=0
    while True:
        racers=input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers=int(racers)
            if 2<=racers<=10:
                print("Number in range.. :)")
                return racers
            else:
                print("Try again Man chose in the range only ...")
                continue
        else:
            print("invalid input enter a number only....")
            print("......................................")
            continue
def __init__turtle():
    screen =turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")

def Create_turtles(colors,racers):
    turtles=[]
    spacing=WIDTH//(racers+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+((i+1)*spacing),(-HEIGHT//2+20))
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles=Create_turtles(colors,racers)
    while True:
        for racer in turtles:
            randoms=random.randint(1,26)
            racer.forward(randoms)
            
            x,y=racer.pos()
            if y>=HEIGHT//2:
                return colors[turtles.index(racer)]
                
        

racers=get_turtle_racers()
__init__turtle()

random.shuffle(COLORS)
colors=COLORS[:racers]            

winner=race(colors)
print ("Winner of the race is: "+ winner)
    


