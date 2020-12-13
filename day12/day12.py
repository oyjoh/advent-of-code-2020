def change_dir(current_dir, action, value):
    value = int(value / 90)
    directions = ['N', 'E', 'S', 'W']
    idx = directions.index(current_dir)
    if action == 'R':
        return directions[(idx + value) % len(directions)]
    else:
        return directions[idx - value]


def move_wp(wp, action, value):
    wp_dir = wp[0]
    wp_val = wp[1]

    if wp_dir != action:
        wp_val -= value
        if wp_val < 0:
            wp_dir = action
            wp_val = abs(wp_val)
    else:
        wp_val += value
    return wp_dir, wp_val


def solve_part_one(data):
    dir_dict = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    current_dir = 'E'

    for line in data:
        action = line[0]
        value = int(line[1:])

        if action == 'F':
            dir_dict[current_dir] += value
        elif action == 'R' or action == 'L':
            current_dir = change_dir(current_dir, action, value)
        else:
            dir_dict[action] += value

    return abs(dir_dict['W'] - dir_dict['E']) + abs(dir_dict['S'] - dir_dict['N'])


def solve_part_two(data):
    ship_pos = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    wp_1 = ('E', 10)
    wp_2 = ('N', 1)

    for line in data:
        action = line[0]
        value = int(line[1:])

        if action == 'F':
            ship_pos[wp_1[0]] += (value * wp_1[1])
            ship_pos[wp_2[0]] += (value * wp_2[1])
        elif action == 'R' or action == 'L':
            wp_1 = (change_dir(wp_1[0], action, value), wp_1[1])
            wp_2 = (change_dir(wp_2[0], action, value), wp_2[1])
        else:
            if action == 'N' or action == 'S':
                if wp_1[0] == 'N' or wp_1[0] == 'S':
                    wp_1 = move_wp(wp_1, action, value)
                else:
                    wp_2 = move_wp(wp_2, action, value)
            elif action == 'E' or action == 'W':
                if wp_1[0] == 'E' or wp_1[0] == 'W':
                    wp_1 = move_wp(wp_1, action, value)
                else:
                    wp_2 = move_wp(wp_2, action, value)
    return abs(ship_pos['W'] - ship_pos['E']) + abs(ship_pos['S'] - ship_pos['N'])


def main():
    data = open('day12.txt', 'r').read().splitlines()

    print(f'Part One: {solve_part_one(data)}')
    print(f'Part Two: {solve_part_two(data)}')


main()
