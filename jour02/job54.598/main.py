from board import Board
from aione import AI_One


def player_play(board, color, player):
    if len(board.get_available_positions()) == 0:
        return board.end_game()

    board.print(color[0])
    player_choice = ''

    if player == 'AI':
        ai = AI_One()
        player_choice = ai.think(board, color)
        print(player_choice)
    else:
        while not player_choice.isnumeric() or not int(player_choice) in board.get_available_positions():
            player_choice = input(f"{player}, choisissez votre position ({','.join([str(i) for i in board.get_available_positions()])})\n\n")
    if board.play(int(player_choice), color):
        return board.end_game(player, color)
    return True

print('Bienvenu dans le jeu du puissance 4, vous devez alignez 4 pions...', end="\n\n")
while True:
    print('Nouvelle Partie:', end="\n\n")
    board = Board(7, 6)

    while True:
        player1_color = ('Rouge', 'R')
        ai_color = ('Jaune', 'J')
        
        if not player_play(board, player1_color, 'joueur 1'):
            break
        if not player_play(board, ai_color, 'AI'):
            break

    if input('Voulez vous continuer ? (o)') != 'o':
        break

print('A+')



    
