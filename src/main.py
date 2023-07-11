import game_logic as gl
import ai_player as ap


# Example usage
m = int(input('Enter a value for m greater than 0: '))
n = int(input('Enter a value for n greater than 0: '))
k = int(input('Enter a value for k greater than 0: '))

ai_player = ap.AIPlayerMCTS('O')
game = gl.MNKGame(m, n, k, ai_player)

game.start()
