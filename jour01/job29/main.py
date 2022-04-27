def round_up(num):
    if num < 40:
        return 'fail'
    for i in range(40, 101, 5):
        if((i - num) in [0, 1, 2]):
            return i
    return num

while True:
    print(round_up(int(input('Choisissez votre note\n'))))