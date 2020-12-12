def valid_grid_pos(y, x, grid):
    if y < 0 or x < 0:
        return False
    if y >= len(grid) or x >= len(grid[0]):
        return False
    return True


def get_num_occupied_adjacent(y, x, grid, long_dist):
    if long_dist:
        return get_num_occupied_adjacent_2(y, x, grid)
    else:
        return get_num_occupied_adjacent_1(y, x, grid)


def get_num_occupied_adjacent_2(y, x, grid):
    occu_count = 0

    north_y, north_x = y - 1, x
    while True:
        if valid_grid_pos(north_y, north_x, grid):
            if grid[north_y][north_x] == '#':
                occu_count += 1
                break
            if grid[north_y][north_x] == 'L':
                break
            north_y -= 1
        else:
            break

    north_west_y, north_west_x = y - 1, x - 1
    while True:
        if valid_grid_pos(north_west_y, north_west_x, grid):
            if grid[north_west_y][north_west_x] == '#':
                occu_count += 1
                break
            if grid[north_west_y][north_west_x] == 'L':
                break
            north_west_x -= 1
            north_west_y -= 1
        else:
            break

    north_east_y, north_east_x = y - 1, x + 1
    while True:
        if valid_grid_pos(north_east_y, north_east_x, grid):
            if grid[north_east_y][north_east_x] == '#':
                occu_count += 1
                break
            if grid[north_east_y][north_east_x] == 'L':
                break
            north_east_y -= 1
            north_east_x += 1
        else:
            break

    east_y, east_x = y, x + 1
    while True:
        if valid_grid_pos(east_y, east_x, grid):
            if grid[east_y][east_x] == '#':
                occu_count += 1
                break
            if grid[east_y][east_x] == 'L':
                break
            east_x += 1
        else:
            break

    west_y, west_x = y, x - 1
    while True:
        if valid_grid_pos(west_y, west_x, grid):
            if grid[west_y][west_x] == '#':
                occu_count += 1
                break
            if grid[west_y][west_x] == 'L':
                break
            west_x -= 1
        else:
            break

    south_y, south_x = y + 1, x
    while True:
        if valid_grid_pos(south_y, south_x, grid):
            if grid[south_y][south_x] == '#':
                occu_count += 1
                break
            if grid[south_y][south_x] == 'L':
                break
            south_y += 1
        else:
            break

    south_west_y, south_west_x = y + 1, x - 1
    while True:
        if valid_grid_pos(south_west_y, south_west_x, grid):
            if grid[south_west_y][south_west_x] == '#':
                occu_count += 1
                break
            if grid[south_west_y][south_west_x] == 'L':
                break
            south_west_y += 1
            south_west_x -= 1
        else:
            break

    south_east_y, south_east_x = y + 1, x + 1
    while True:
        if valid_grid_pos(south_east_y, south_east_x, grid):
            if grid[south_east_y][south_east_x] == '#':
                occu_count += 1
                break
            if grid[south_east_y][south_east_x] == 'L':
                break
            south_east_y += 1
            south_east_x += 1
        else:
            break
    return occu_count


def get_num_occupied_adjacent_1(y, x, grid):
    occu_count = 0

    north_y, north_x = y - 1, x
    if valid_grid_pos(north_y, north_x, grid):
        if grid[north_y][north_x] == '#':
            occu_count += 1

    north_west_y, north_west_x = y - 1, x - 1
    if valid_grid_pos(north_west_y, north_west_x, grid):
        if grid[north_west_y][north_west_x] == '#':
            occu_count += 1

    north_east_y, north_east_x = y - 1, x + 1
    if valid_grid_pos(north_east_y, north_east_x, grid):
        if grid[north_east_y][north_east_x] == '#':
            occu_count += 1

    east_y, east_x = y, x + 1
    if valid_grid_pos(east_y, east_x, grid):
        if grid[east_y][east_x] == '#':
            occu_count += 1

    west_y, west_x = y, x - 1
    if valid_grid_pos(west_y, west_x, grid):
        if grid[west_y][west_x] == '#':
            occu_count += 1

    south_y, south_x = y + 1, x
    if valid_grid_pos(south_y, south_x, grid):
        if grid[south_y][south_x] == '#':
            occu_count += 1

    south_west_y, south_west_x = y + 1, x - 1
    if valid_grid_pos(south_west_y, south_west_x, grid):
        if grid[south_west_y][south_west_x] == '#':
            occu_count += 1

    south_east_y, south_east_x = y + 1, x + 1
    if valid_grid_pos(south_east_y, south_east_x, grid):
        if grid[south_east_y][south_east_x] == '#':
            occu_count += 1
    return occu_count


def update_grid(grid, seat_rule, long_dist):
    new_grid = []
    for line in grid:
        new_grid.append(line.copy())
    # new_grid = grid.copy()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid_object = grid[y][x]
            # print(grid_object)
            if grid_object == '.':
                continue
            if grid_object == 'L':
                if get_num_occupied_adjacent(y, x, grid, long_dist) == 0:
                    new_grid[y][x] = '#'
            if grid_object == '#':
                if get_num_occupied_adjacent(y, x, grid, long_dist) >= seat_rule:
                    new_grid[y][x] = 'L'

    return new_grid


def count_occupied_seats(grid):
    occupied_seats = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid_object = grid[y][x]
            if grid_object == '#':
                occupied_seats += 1
    return occupied_seats


def solve(grid, seat_rule, long_dist):
    prev_seat = -1
    current_grid = grid
    while True:
        new_grid = update_grid(current_grid, seat_rule, long_dist)
        occupied_seats = count_occupied_seats(new_grid)
        if occupied_seats == prev_seat:
            prev_seat = occupied_seats
            current_grid = new_grid
            break
        else:
            prev_seat = occupied_seats
            current_grid = new_grid

    return prev_seat


def main():
    data = open('day11.txt', 'r').read().splitlines()
    data = list(map(list, data))

    print(f'Part One: {solve(data, seat_rule=4, long_dist=False)}')
    print(f'Part Two: {solve(data, seat_rule=5, long_dist=True)}')


main()
