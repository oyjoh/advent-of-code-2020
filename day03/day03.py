import math


def solve(data, delta_x, delta_y):
    x_coord = 0
    y_coord = 0
    tree_count = 0

    while y_coord < len(data):
        if data[y_coord][x_coord % len(data[y_coord])] == '#':
            tree_count = tree_count + 1
        x_coord += delta_x
        y_coord += delta_y
    return tree_count


data = open('day03.txt', 'r').read().splitlines()

print(f'Part One: {solve(data, 3, 1)}')

delta_x_y = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(f'Part Two: {math.prod(map(lambda dt: solve(data, dt[0], dt[1]), delta_x_y))}')
