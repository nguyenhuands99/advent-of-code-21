
with open('input.txt', 'r') as file:
    depth = 0
    horizon = 0
    aim = 0
    for line in file:
        direc, val = line.split(' ')
        if direc == 'forward':
            horizon += int(val)
            depth += int(aim) * int(val)
        elif direc == 'down':
            aim += int(val)
        elif direc == 'up':
            aim -= int(val)
        else:  # if anything wrong outside cases
            continue
    print(f'depth = {depth}, horizon = {horizon}, mul = {depth * horizon}')
