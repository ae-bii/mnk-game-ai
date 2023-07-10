class MNKGame:
    def __init__(self, m, n, k, ai_player):
        self.m = m
        self.n = n
        self.k = k
        self.board = [[' ' for i in range(n)] for j in range(m)]
        self.valid_moves = [[1 for i in range(n)] for j in range(m)]
        self.current_player = 'X'
        self.ai_player = ai_player

    def start(self):

        while not self.is_game_over():
            self.print_board()

            # Human player's turn
            while True:
                row = int(input('Enter the row (0 to {}): '.format(self.m - 1)))
                col = int(
                    input('Enter the column (0 to {}): '.format(self.n - 1)))
                if self.make_move(row, col):
                    break
                print('Invalid move. Try again.')
                print()

            if self.is_game_over():
                break

            # AI player's turn
            row, col = self.ai_player.get_move(self)
            self.make_move(row, col)

        self.print_board()
        winner = self.get_winner()
        if winner:
            print('Player', winner, 'wins!')
        else:
            print('It\'s a draw!')

    def print_board(self):
        print()
        for row in self.board:
            print('|'.join(row))
        print()

    def is_valid_move(self, row, col):
        return not (row < 0 or row >= self.m or col < 0 or col >= self.n) and self.valid_moves[row, col]

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.valid_moves[row][col] = 0
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
