from board import Board

def player_play(board, color, player):
    if len(board.get_available_positions()) == 0:
        return board.end_game(player, color)

    board.print(color[0])
    player_choice = ''

    while not player_choice.isnumeric() or not int(player_choice) in board.get_available_positions():
        player_choice = input(f"{player}, choisissez votre position ({','.join([str(i) for i in board.get_available_positions()])})\n\n")
    if board.play(int(player_choice), color):
        print(f'{player} ({color[1]}) a gagné 100k bravo à lui')
        return False
    return True
    

print('Bienvenu dans le jeu du puissance 4, vous devez alignez 4 pions...', end="\n\n")
while True:
    print('Nouvelle Partie:', end="\n\n")
    board = Board(7, 6)

    while True:
        player1_color = ('Rouge', 'R')
        player2_color = ('Jaune', 'J')
        
        if not player_play(board, player1_color, 'joueur 1'):
            break
        if not player_play(board, player2_color, 'joueur 2'):
            break

    if input('Voulez vous continuer ? (o)') != 'o':
        break

print('A+')