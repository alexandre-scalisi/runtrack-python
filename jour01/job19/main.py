def draw_rectangle(width, height):
    for i in range(height):
        middle = ' '
        if i == 0 or i == height -1:
            middle = '-' * (width - 2)
        print('|' + middle + '|')

draw_rectangle(3,3)