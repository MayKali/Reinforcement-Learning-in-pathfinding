# Simulation.py 
#Absorbing Goal - Q-learning 
import Network
import threading
import time
import matplotlib.pyplot as plt
import numpy as np 
import random

epsilon = 0.2  #epsilon-greedy policy  - exploration parameter
gamma = 0.3 #Parameter that determines how much each future reward is taken into consideration
            # If gamma is close to 0, we only care about immediate rewards  
alpha = 1.0 #Learning Rate
actions = Network.actions
states = []

Q = {}
for i in range(Network.x):
    for j in range(Network.y):
        states.append((i, j))

for state in states:
    blank = {}
    for action in actions:
        
    
        blank[action] = 0

    Q[state] = blank

for (i, j, c, w) in Network.goal:
    for action in actions:
        Q[(i, j)][action] = w

#Position_Bf refers to current state and _Af refers to next state


def do_action(action):
    Position_Bf = Network.player_location
    rew = -Network.score
    if action == actions[0]:
        Network.try_move(0, -1)
    elif action == actions[1]:
        Network.try_move(0, 1)
    elif action == actions[2]:
        Network.try_move(-1, 0)
    elif action == actions[3]:
        Network.try_move(1, 0)
    else:
        return
    Position_Af = Network.player_location
    rew += Network.score
    return Position_Bf, action, rew, Position_Af

'''
def policy(max_act):
    if random.random()> epsilon:
        return max_act
    else:
        random_idx= random.randint(0,len(actions)-2)
        if actions[random_idx] == max_act:
            return actions[len(actions)-1]
        else:
            return actions[random_idx]
'''

def max_Q(Position_Bf):
    val = None 
    act = None
    for a, q in Q[Position_Bf].items():
        if val is None or (q > val):
            val = q
            act = a
    return act, val


def inc_Q(Position_Bf, a, alpha, inc): 
    Q[Position_Bf][a] *= 1 - alpha
    Q[Position_Bf][a] += alpha * inc

episodes= []

def run():
    global gamma
    time.sleep(1)
    alpha = 1
    episode = 1.0
    

    while True:
        # Pick the right action
        Position_Bf = Network.player_location
        max_act, max_val = max_Q(Position_Bf)
        '''chosen_act = policy(max_act)'''
        (Position_Bf, a, rew, Position_Af) = do_action(max_act)

        # Update Q
        max_act, max_val = max_Q(Position_Af)
        inc_Q(Position_Bf, a, alpha, rew + gamma * max_val)

        # Check if the game has restarted
        episode += 1.0
        if Network.has_restarted():
            Network.restart_game()
            time.sleep(0.01)
            t = episode

        # Update the learning rate
        alpha = pow(episode, -0.1)

        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.1)
        episodes.append(episode)



t = threading.Thread(target=run)
t.daemon = True
t.start()
Network.start_game()

