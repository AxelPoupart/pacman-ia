# pacman-ia
Graph search for fastest pacman 

## Overview

Using a online code of the game pacman, I manage to implement algorithms that helps Pacman find his path to his food.

To do that I implement simples algorithms like DFS and BFS. Pacman know only the case that are next to him. Using those algorithms he found out the shortest path, which is the compute in the game and the pacman takes the shortest path to his food.

On this maze, pacman has explore almost all of the maze to find out the food. The color represent the depth of the node during DFS, if it remains black this mean the node has never been explored

![Maze](./Images/maze.png)

The function I modified are mostly in the search/search.py file
