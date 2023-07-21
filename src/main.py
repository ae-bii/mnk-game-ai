import game_logic as gl
import ai_player as ap


# Example usage
m = int(input('Enter a value for m greater than 0 (Default = 3): ') or '3')
n = int(input('Enter a value for n greater than 0 (Default = 3): ') or '3')
k = int(input('Enter a value for k greater than 0 (Default = 3): ') or '3')

choose_ai = """
1. Random
2. Minimax with Alpha-Beta Pruning
3. Monte-Carlo Tree Search
"""

print(choose_ai)
ai_index = int(input('Choose an AI opponent (1-3 or Default = 1): ') or '1') - 1

ai_players = [ap.AIPlayerRandom('O'), ap.AIPlayerMinimax('O'), ap.AIPlayerMCTS('O')]

ai_player = ai_players[ai_index]
game = gl.MNKGame(m, n, k, ai_player)

game.start()
