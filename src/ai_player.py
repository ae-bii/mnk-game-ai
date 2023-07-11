import math
import random
import numpy as np

"""
AI which does random moves
"""
class AIPlayerRandom:
    def __init__(self, symbol):
        self.symbol = symbol
    
    """
    Generates a random valid move
    """
    def get_move(self, game):
        m = game.m
        n = game.n

        row = random.randrange(m)
        col = random.randrange(n)

        while not game.is_valid_move(row, col):
            row = random.randrange(m)
            col = random.randrange(n)

        return row, col


"""
AI that uses the minimax algorithm with alpha-beta pruning to make the optimal move
"""
class AIPlayerOptimal:
    def __init__(self, symbol):
        self.symbol = symbol

    """
    Generates the optimal move
    """
    def get_move(self, game):
        _, move = self.minimax(game, True, -math.inf, math.inf)
        return move

    """
    Uses the minimax algorithm to calculate the optimal move
    """
    def minimax(self, game, maximizing_player, alpha, beta):
        if game.is_game_over():
            winner = game.get_winner()
            if winner == self.symbol:
                return 1, None
            elif winner:
                return -1, None
            else:
                return 0, None

        if maximizing_player:
            max_score = -math.inf
            best_move = None
            for row in range(game.m):
                for col in range(game.n):
                    if game.is_valid_move(row, col):
                        game.make_move(row, col)
                        score, _ = self.minimax(game, False, alpha, beta)
                        game.board[row][col] = ' '
                        game.current_player = 'O' if game.current_player == 'X' else 'X'
                        if score > max_score:
                            max_score = score
                            best_move = (row, col)
                        alpha = max(alpha, score)
                        if alpha >= beta:
                            break
            return max_score, best_move
        else:
            min_score = math.inf
            best_move = None
            for row in range(game.m):
                for col in range(game.n):
                    if game.is_valid_move(row, col):
                        game.make_move(row, col)
                        score, _ = self.minimax(game, True, alpha, beta)
                        game.board[row][col] = ' '
                        game.current_player = 'O' if game.current_player == 'X' else 'X'
                        if score < min_score:
                            min_score = score
                            best_move = (row, col)
                        beta = min(beta, score)
                        if alpha >= beta:
                            break
            return min_score, best_move

"""
AI that uses the Monte-Carlo Tree Search Algorithm to find the next optimal move
"""
class AIPlayerMCTS:
    def __init__(self, symbol):
        self.symbol = symbol

    """
    Runs the simulations to get the optimal move
    """
    def get_move(self, game):
        # Number of simulations to run for each valid move
        num_simulations = 100

        # Get all valid moves
        valid_moves = [(i, j) for i in range(game.m) for j in range(game.n) if game.is_valid_move(i, j)]

        # Run simulations for each valid move and keep track of scores
        scores = []
        for move in valid_moves:
            score = 0
            for _ in range(num_simulations):
                # Copy the game and make the move
                simulation_game = game.copy()
                simulation_game.make_move(*move)

                # Run a random simulation from the new state
                while not simulation_game.is_game_over():
                    # Get all valid moves for the simulation game
                    valid_moves_simulation = [(i, j) for i in range(simulation_game.m) for j in range(simulation_game.n) if simulation_game.is_valid_move(i, j)]
                    # Choose a random move and make it
                    random_move = random.choice(valid_moves_simulation)
                    simulation_game.make_move(*random_move)

                # Check the result of the simulation
                winner = simulation_game.get_winner()
                if winner == self.symbol:
                    score += 1
                elif winner is None:
                    score += 0.5

            scores.append(score)

        # Choose the move with the highest average score
        best_move = valid_moves[scores.index(max(scores))]

        return best_move