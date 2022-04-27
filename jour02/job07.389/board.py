class Board:
    def __init__(self, i, j):
        self.width = i
        self.height = j
        self.board = [['O'] * i for _ in range(j)]

    def get_available_positions(self):
        available_positions = []
        for i in range(self.width):
            if self.board[0][i] == "O":
                available_positions.append(i)
        return 
        
    def end_game(self, player = None, color = None):
        print()
        for i in range(self.height):
            print(f'{self.board[i]}')
        
        if player:
            print(f'\n{player} ({color[1]}) a gagné 100k bravo à lui', end='\n\n')
        else:
            print('Match Nul', end='\n\n')
        return False
   
    def play(self, position, color):
        for i in range(self.height - 1, -1, -1):
            if self.board[i][position] == 'O':
                self.board[i][position] = color[1]
                break
        return self.check_if_winner(color[1])


    def print(self, letter):
        print("\nPlateau actuel:", end="\n\n")
        print(''.join([f"  {str(i) if i in self.get_available_positions() else ' '}  "for i in range(self.width)]))
        for i in range(self.height):
            print(self.board[i])
        print(f"\nPion actuel: {letter}", end="\n\n")

        
    def check_if_winner(self, letter):
        to_find = [letter] * 4
        for i in range(self.height - 1, -1, -1):
            for j in range(self.width):
                # Horizontal
                if self.board[i][j:j+4] == to_find:
                    return True
                # Vertical
                if [a[j] for a in self.board[i:(i-4) if i >= 4 else None:-1]] == to_find:
                    return True
                # Diagonal /  
                if [a[j+index] for index, a in enumerate(self.board[i:(i-4) if i >= 4 else None:-1]) if j + index < self.width] == to_find:
                    return True
                # Diagonal \
                if [a[self.width-1-j-index] for index, a in enumerate(self.board[i:(i-4) if i >= 4 else None:-1]) if self.width-1-j-index >= 0] == to_find:
                    return True
                
        return False