from turtle import width


file = open('maze.mz.txt', 'r')

maze = []


def read_file_recursive(f):
    cur_line = f.readline()
    if not cur_line:
        return
    cur_line_array = list(cur_line)
    cur_line_array.pop()
    maze.append(cur_line_array)
    read_file_recursive(f)


read_file_recursive(file)
# maze.append(list(file.readline()))
file.close()

height = len(maze)
width = len(maze[0])

print(width, height)

shortest = {}
visited = {}


def find_way(x, y, level, coordinates=[]):
    global shortest
    if (shortest.get('level') and level > shortest.get('level')) or x < 0 or x >= height or y < 0 or y >= width or (x, y) in coordinates or maze[x][y] == '#' or (visited.get((x, y)) and visited.get((x, y)) <= level):
        return
    if x >= height - 1 and y >= width - 1:
        shortest['coordinates'] = [*coordinates, (x, y)]
        shortest['level'] = level
        return

    visited[(x, y)] = level

    find_way(x, y-1, level + 1, [*coordinates, (x, y)])
    find_way(x, y+1, level + 1, [*coordinates, (x, y)])
    find_way(x-1, y, level + 1, [*coordinates, (x, y)])
    find_way(x+1, y, level + 1, [*coordinates, (x, y)])


find_way(0, 0, 0)

file = open('completed_maze.mz.txt', 'w')


def draw_completed_maze(x, y, f, best, maze):
    if x >= height:
        return
    draw_line(x, y, f, best, maze)
    draw_completed_maze(x + 1, y, f, best, maze)


def draw_line(x, y, f, best, maze):
    if y >= width:
        f.write('\n')
        return

    if (x, y) in best:
        f.write('X')
    else:
        f.write(maze[x][y])

    draw_line(x, y + 1, f, best, maze)


draw_completed_maze(0, 0, file, shortest['coordinates'], maze)

file.close()
