# *m,n,k*-game AI

This project is an implementation of an *m,n,k* game in Python. The game is played on an *m*×*n* board with two players. The players take turns to place their symbol on the board, and the goal is to be the first to get *k* of their symbols in a row, either horizontally, vertically, or diagonally.

## Features

- The game is terminal-based and interactive, providing clear instructions and feedback to the user.
- The game includes an AI opponent that uses one of three strategies: random moves, minimax algorithm with alpha-beta pruning, or Monte Carlo Tree Search (MCTS).
- The AI is designed to be interchangeable, allowing for easy comparison of different strategies.
- The game implements comprehensive game state evaluations, checking for the validity of moves, the end of the game, and the winning player.
- The AI fastest player is currently MCTS as it is probibalistic while the slowest is Minimax.

## AI Strategies

### Random Moves

The AI chooses a valid move at random.

### Minimax Algorithm with Alpha-Beta Pruning

The AI uses the minimax algorithm to explore the game tree up to a certain depth and evaluate the game states. Alpha-beta pruning is used to reduce the number of nodes that are evaluated by the minimax algorithm, significantly improving the efficiency of the AI.

### Monte Carlo Tree Search (MCTS)

The AI uses MCTS to make its move. This algorithm uses probabilistic simulations of potential games to evaluate the game states and make a decision. The MCTS algorithm consists of four steps: Selection, Expansion, Simulation, and Backpropagation.

## How to Run the Game

To run the game, execute the `main.py` script in Python. The game will start, and the user will be prompted to choose their settings.

## Contributions

Contributions to this project are welcome. If you find a bug or would like to make an improvement, please open an issue or submit a pull request.
