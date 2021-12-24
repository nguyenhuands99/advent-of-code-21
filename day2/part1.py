

with open('input.txt', 'r') as file:
    depth = 0
    horizon = 0
    for line in file:
        direc, val = line.split(' ')
        if direc == 'forward':
            horizon += int(val)
        elif direc == 'down':
            depth += int(val)
        elif direc == 'up':
            depth -= int(val)
        else:  # if anything wrong outside cases
            continue
    print(f'depth = {depth}, horizon = {horizon}, mul = {depth * horizon}')
