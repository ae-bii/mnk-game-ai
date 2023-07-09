import math
import random

"""
AI which does random moves
"""
class AIPlayerRandom:
    def __init__(self, symbol):
        self.symbol = symbol
        
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

    def get_move(self, game):
        _, move = self.minimax(game, True, -math.inf, math.inf)
        return move

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
