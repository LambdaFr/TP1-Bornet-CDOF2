# TP1-Bornet-CDOF2
# Python Snake Game

This is a simple implementation of the classic Snake game in Python.

## Installation

1. Clone this repository: `git clone https://github.com/LambdaFr/TP1-Bornet-CDOF2.git`
2. Go to the project directory: `cd TP1-Bornet-CDOF2`
3. Setup the project: `python setup.py install`
4. Launche the game: `python tp1.py`

## How to play

For now the game is simple :
Directionnal keys allow you to go up, down, left and right. You have to eat the red square to grow without touching yourself or the border.

## Problems solved : 
Pause and Resume Functionality:

Implemented a pause menu accessible by pressing the ESC key during the game.
Options in the pause menu include Resume, Restart, and Main Menu.
The msvcrt library is used for detecting key presses.
Game Start Interface:

Added an interface at the beginning of the game to start or quit.
Player won't start directly controlling the snake upon launching the game.
Scoring System:

Introduced a scoring system where the player earns one point for each red square (food) eaten.
Map Size Increase:

Increased the size of the map to provide a larger playing area.
Red Square Placement:

Ensured that the red square (food) spawns only in free squares, without any part of the snake on it.

## Authors

Joshua Bornet - Headmaster\
Anouk Leyris\
Jean-Baptiste Martin

