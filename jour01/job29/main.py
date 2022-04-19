def round_up(num):
    if num < 40:
        return 'fail'
    for i in range(40, 101, 5):
        if((i - num) in [0, 1, 2]):
            return i
    return num

print(round_up(93))