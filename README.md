# conway-game-of-life
This game is a cellular automaton devised by the mathematician John Conway to highlight that the evolution is determined by an initial state.


The Game of Life, a.k.a. Life, is a cellular automaton conceptulaized by the British Mathematician John Horton Conway in 1970.
It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.
This game starts with a random state of cells that propogate into interesting patterns and outcomes.
It is Turing complete and can simulate a universal constructor or any other Turing machine.

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

With these ground rules laid out, this Python implementation is very expandable and auto-complies to a .gif for easy viewing

# Requirements
Python3, imageio, and locally installed LaTeX compilier (Comment out the plt.rc() properties to avoid installation)
