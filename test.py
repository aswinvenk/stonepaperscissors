from src.spsgamepkg import game
aswin_game=game.Game('Aswin')
venkat_game=game.Game('Venkat')

print(game.__version__)
print(game.__author__)
game.rules()

# to play the game
aswin_game.game(2)
# to display the result
aswin_game.display_result()
# to reset the score
aswin_game.clear_score()

# to play the game
venkat_game.game(2)
# to display the result
venkat_game.display_result()
# to reset the score
venkat_game.clear_score()