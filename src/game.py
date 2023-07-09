import random

class MNKGame:
    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
        self.board = [[' ' for _ in range(n)] for _ in range(m)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
        print()

    def is_valid_move(self, row, col):
        if row < 0 or row >= self.m or col < 0 or col >= self.n:
            return False
        if self.board[row][col] != ' ':
            return False
        return True

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def is_game_over(self):
        return self.get_winner() or self.is_board_full()

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def get_winner(self):
        for row in range(self.m):
            for col in range(self.n):
                if self.board[row][col] == ' ':
                    continue

                # Check horizontal
                if col + self.k <= self.n:
                    if all(self.board[row][col+i] == self.board[row][col] for i in range(self.k)):
                        return self.board[row][col]

                # Check vertical
                if row + self.k <= self.m:
                    if all(self.board[row+i][col] == self.board[row][col] for i in range(self.k)):
                        return self.board[row][col]

                # Check diagonal
                if col + self.k <= self.n and row + self.k <= self.m:
                    if all(self.board[row+i][col+i] == self.board[row][col] for i in range(self.k)):
                        return self.board[row][col]

                # Check anti-diagonal
                if col - self.k >= -1 and row + self.k <= self.m:
                    if all(self.board[row+i][col-i] == self.board[row][col] for i in range(self.k)):
                        return self.board[row][col]

        return None

class AIPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        m = game.m
        n = game.n
        for row in range(m):
            for col in range(n):
                if game.is_valid_move(row, col):
                    return row, col

# Example usage
m = 3
n = 3
k = 3

game = MNKGame(m, n, k)
ai_player = AIPlayer('O')

while not game.is_game_over():
    game.print_board()

    # Human player's turn
    while True:
        row = int(input('Enter the row (0 to {}): '.format(m - 1)))
        col = int(input('Enter the column (0 to {}): '.format(n - 1)))
        if game.make_move(row, col):
            break
        print('Invalid move. Try again.')

    if game.is_game_over():
        break

    # AI player's turn
    row, col = ai_player.get_move(game)
    game.make_move(row, col)

game.print_board()
winner = game.get_winner()
if winner:
    print('Player', winner, 'wins!')
else:
    print('It\'s a draw!')
