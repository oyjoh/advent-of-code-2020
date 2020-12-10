entries = []

with open('day01.txt', 'r') as inp:
    data = inp.read().splitlines()

for line in data:
    entries.append(int(line))


def part_one(entries):
    for x_idx, x in enumerate(entries):
        for y_idx, y in enumerate(entries):
            if x_idx != y_idx:
                if x + y == 2020:
                    return x * y


def part_two(entries):
    for x_idx, x in enumerate(entries):
        for y_idx, y in enumerate(entries):
            for z_idx, z in enumerate(entries):
                if x_idx != y_idx != z_idx:
                    if x + y + z == 2020:
                        return x * y * z


print(f'Part One: {part_one(entries)}')
print(f'Part Two: {part_two(entries)}')
