def draw_triangle(height):
    for i in range(height):
        space_between = " "
        if i == height -1:
            space_between = '_'
        print(' ' * (height - i), end='')
        print('/', end='')
        print(space_between * i * 2, end='')
        print('\\')

draw_triangle(5)