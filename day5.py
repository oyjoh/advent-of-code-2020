def get_lower_half(a_list):
    half = len(a_list) // 2
    return a_list[:half]


def get_upper_half(a_list):
    half = len(a_list) // 2
    return a_list[half:]


def solve(num_rows, row_len, boardingpass):
    rows = list(range(0, num_rows))
    seats = list(range(0, row_len))

    for char in boardingpass:
        if char == 'F':
            rows = get_lower_half(rows)
        elif char == 'B':
            rows = get_upper_half(rows)
        elif char == 'R':
            seats = get_upper_half(seats)
        elif char == 'L':
            seats = get_lower_half(seats)
        else:
            print('invalid input')
    return (rows[0] * 8) + seats[0]


data = open('day5.txt', 'r').read().splitlines()

seat_ids = []
for boardingpass in data:
    seat_ids.append(solve(128, 8, boardingpass))

print(f'Part One: {max(seat_ids)}')
print(f'Part Two: {max(set(range(min(seat_ids), max(seat_ids) + 1)).difference(seat_ids))}')
