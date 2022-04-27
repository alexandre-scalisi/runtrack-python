

size = 8

globalArray = []
print(globalArray)
win = []
def fill_array(x, y):
    if x >= size:
        return
    if y >= size:
        fill_array(x + 1, 0)
        return
    if y == 0:
        globalArray.append([])
    globalArray[x].append('O')
    fill_array(x, y + 1)

fill_array(0, 0)

def queen(x, y, arr):
    global win
    if len(win) > 0:
        return
    if x == size:
        win = arr
        return

    if y >= size and check_left(x, y - 1, [*arr]):
        return False
    if y >= size:
        x += 1
        y = 0

    if check_top_left(x - 1, y - 1, [*arr]) and check_left(x, y - 1, [*arr]) and check_top(x - 1, y, [*arr]) and check_top_right(x - 1, y + 1, [*arr]):
        arr[x][y] = 'X'
        queen(x + 1, 0, [*arr])
        if len(win) > 0:
            return
        arr[x][y] = 'O'

    queen(x, y + 1, [*arr])


def check_top_left(x, y, arr):
    if x < 0 or y < 0:
        return True

    if arr[x][y] == 'X':
        return False

    return check_top_left(x - 1, y - 1, [*arr])


def check_top(x, y, arr):
    if x < 0:
        return True

    if arr[x][y] == 'X':
        return False

    return check_top(x - 1, y, [*arr])


def check_top_right(x, y, arr):
    if x < 0 or y >= size:
        return True

    if arr[x][y] == 'X':
        return False

    return check_top_right(x - 1, y + 1, [*arr])


def check_left(x, y, arr):
    if y < 0:
        return True

    if arr[x][y] == 'X':
        return False

    return check_left(x, y - 1, [*arr])


queen(0, 0, [*globalArray])
for i in range(size):
    for j in range(size):
        print(win[i][j], end=' ')
    print()
