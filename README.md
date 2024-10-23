# Turtle Crossing Game

This project is a simple **Turtle Crossing Game** implemented in Python using the `turtle` graphics library. The player controls a turtle, attempting to cross a road filled with moving cars. The objective is to reach the top of the screen without colliding with any cars. Each successful crossing increases the game level, and the speed of the cars increases as well.

## Features

- **Player Movement**: Control the turtle by pressing the "Up" key to move forward.
- **Car Generation**: Randomly generated cars that move from right to left.
- **Scoreboard**: Displays the current level and shows "Game Over" when the player collides with a car.
- **Game Leveling**: Every time the turtle reaches the top of the screen, the game levels up, and the car speed increases.

## Prerequisites

Before running the game, make sure you have Python installed along with the `turtle` module (which is included with Python by default).

## Gameplay Instructions

- **Control the Turtle**: Use the "Up" arrow key to move the turtle forward.
- **Objective**: Reach the top of the screen without colliding with any cars.
- **Level Up**: Each time the turtle successfully crosses to the top, the game levels up, and the car speed increases.
- **Game Over**: The game ends if the turtle collides with a car.

## Code Overview

### `main.py`

- Sets up the game screen using `turtle.Screen()`.
- Initializes the player, car manager, and scoreboard.
- Contains the main game loop, which updates the game state, creates new cars, moves cars, checks for collisions, and handles the game's end condition.

### `Player` Class (`player.py`)

- Inherits from `Turtle` and is used to create and control the turtle character.
- Includes methods for moving the turtle forward and checking if it has reached the top of the screen.

### `CarManager` Class (`car_manager.py`)

- Manages the generation and movement of cars.
- Cars are generated randomly and move from the right side of the screen to the left.
- The speed of the cars increases as the player levels up.

### `Scoreboard` Class (`scoreboard.py`)

- Displays the current game level and handles the game-over sequence.
- Updates the level after each successful crossing.
