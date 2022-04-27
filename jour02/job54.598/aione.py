import random

class AI_One:
    def __init__(self):
        pass
    
    def think(self, board, color):
        return random.choice(board.get_available_positions())