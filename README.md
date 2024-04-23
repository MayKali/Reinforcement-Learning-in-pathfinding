# Python - Reinforcement Learning

A mini-project I did in the Summer of 2018 implementing reinforcement learning to pathfinding with obstacles. 

# Q-Learning Grid Game

This project consists of two Python scripts, `Network.py` and `Simulation.py`, that work together to implement a grid-based game using Q-Learning, a type of Reinforcement Learning algorithm.

## Network.py

`Network.py` sets up the game environment. It uses the Tkinter library to create a graphical user interface for the game. The game is played on a grid where each cell can be either an obstacle, a goal, or a free space. The player navigates through the grid, avoiding obstacles and aiming to reach the goal. The game uses a reward system to encourage reaching the goal and penalizes each step taken to encourage efficiency. The game can be restarted once the goal is reached.

## Simulation.py

`Simulation.py` implements the Q-Learning algorithm. It uses the game environment set up in `Network.py` and learns to navigate through the grid to reach the goal while avoiding obstacles. The learning process involves exploring the environment, observing the rewards or penalties received, and updating a Q-table, which guides the player's actions. The Q-Learning parameters include:

- `epsilon`: The exploration parameter for the epsilon-greedy policy.
- `gamma`: The discount factor that determines how much future rewards are taken into consideration.
- `alpha`: The learning rate.

The Q-Learning algorithm runs in a loop, continuously updating the Q-table and navigating the player through the grid based on the current Q-table. The learning rate decreases over time, allowing the algorithm to explore the environment thoroughly in the early stages and exploit its learned knowledge in the later stages.

## Running the Game

To run the game, simply execute the `Simulation.py` script. This will start the game interface and the Q-Learning algorithm.

Please note that this is a simple implementation of Q-Learning and was created as a fun little project after my 1st year of undergrad. 

## Dependencies

- Python 3.x
- Tkinter
- Matplotlib
- Numpy

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto
- The Q-Learning algorithm



![https://github.com/MayKali/Reinforcement-Learning-in-pathfinding/blob/master/images/Test.gif)](https://github.com/MayKali/Reinforcement-Learning-in-pathfinding/blob/master/images/Test.gif)
