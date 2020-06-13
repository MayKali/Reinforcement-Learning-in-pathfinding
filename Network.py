#Q-Learning
import random
from tkinter import *
root = Tk()

#Understood

pixel = 50
(x, y) = (7, 7) #Number of blocks
actions = ["up", "down", "left", "right"]



gameDisplay = Canvas(root, width=x*pixel, height=y*pixel) #GameDisplay
player_location = (0, y-1) #Start location of the player 
score = 1
restart = False #While loop 
step_penalty = -0.05 #Reward for taking one step 

obstacles = [(1,0),(1,1),(0,0),(2,5),(2,6)] #FIGURE A WAY TO RANDOMIZE THESE OBSTACLES 
goal = [(4, 0, "green", 1)] #Goal and Trap


'''(4, 1, "red", -1)'''
def Anon(i, j, action): #Directions

    if action == actions[0]:
        return gameDisplay.create_polygon((i+0.5-0.1)*pixel, (j+0.1)*pixel,
                                    (i+0.5+0.1)*pixel, (j+0.1)*pixel,
                                    (i+0.5)*pixel, j*pixel,
                                    fill="white", width=1)
    elif action == actions[1]:
        return gameDisplay.create_polygon((i+0.5-0.1)*pixel, (j+1-0.1)*pixel,
                                    (i+0.5+0.1)*pixel, (j+1-0.1)*pixel,
                                    (i+0.5)*pixel, (j+1)*pixel,
                                    fill="white", width=1)
    elif action == actions[2]:
        return gameDisplay.create_polygon((i+0.1)*pixel, (j+0.5-0.1)*pixel,
                                    (i+0.1)*pixel, (j+0.5+0.1)*pixel,
                                    i*pixel, (j+0.5)*pixel,
                                    fill="white", width=1)

    elif action == actions[3]:
        return gameDisplay.create_polygon((i+1-0.1)*pixel, (j+0.5-0.1)*pixel,
                                    (i+1-0.1)*pixel, (j+0.5+0.1)*pixel,
                                    (i+1)*pixel, (j+0.5)*pixel,
                                    fill="white", width=1)  


#Understood
def create_background():
    global goal, obstacles, pixel, x, y, player_location
    for i in range(x):
        for j in range(y):
            gameDisplay.create_rectangle(i*pixel, j*pixel, (i+1)*pixel, (j+1)*pixel, fill="white", width =1)
            #Grid background
            temp = {}

            for action in actions:
                temp[action] = Anon(i, j, action)
            
    for (i, j, c, w) in goal:
        gameDisplay.create_rectangle(i*pixel, j*pixel, (i+1)*pixel, (j+1)*pixel, fill=c, width=1)
    for (i, j) in obstacles:
        gameDisplay.create_rectangle(i*pixel, j*pixel, (i+1)*pixel, (j+1)*pixel, fill="black", width=1)

create_background()


scores = []

def try_move(dx, dy):
    global player_location, x, y, score, step_penalty, player, restart
    if restart == True:
        restart_game()
    x_N = player_location[0] + dx
    y_N = player_location[1] + dy
    score += step_penalty
    if (x_N >= 0) and (x_N < x) and (y_N >= 0) and (y_N < y) and not ((x_N, y_N) in obstacles):
        gameDisplay.coords(player, x_N*pixel+pixel*2/10, y_N*pixel+pixel*2/10, x_N*pixel+pixel*8/10, y_N*pixel+pixel*8/10)
        player_location = (x_N, y_N)
    for (i, j, c, w) in goal:
        if x_N == i and y_N == j:
            
            score += w
            scores.append(score)
            if score > 0:
                print("Nice Job! Your score is: ", score)
            else:
                print ("Well I just wasted my time, Your score is: ", score)
            restart = True
            return
 


def up(event):
    try_move(0, -1)


def down(event):
    try_move(0, 1)


def left(event):
    try_move(-1, 0)


def right(event):
    try_move(1, 0)


def restart_game():
    global player_location, score, player, restart
    player_location = (0, y-1)
    score = 1
    restart = False
    gameDisplay.coords(player, player_location[0]*pixel+pixel*2/10, player_location[1]*pixel+pixel*2/10, player_location[0]*pixel+pixel*8/10, player_location[1]*pixel+pixel*8/10)

def has_restarted():
    return restart

root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Right>", right)
root.bind("<Left>", left)

gameDisplay.grid(row=0, column=0)


player = gameDisplay.create_rectangle(player_location[0]*pixel+pixel*2/10, player_location[1]*pixel+pixel*2/10,
                            player_location[0]*pixel+pixel*8/10, player_location[1]*pixel+pixel*8/10, fill="blue", width=1, tag="player")

def start_game():
    root.mainloop()



