def part_two(data):
    count = 0
    for line in data:
        sub = line.split()
        bounds = sub[0].split('-')

        idx_1 = int(bounds[0])
        idx_2 = int(bounds[1])

        target = sub[1].replace(':', '')

        input_string = sub[2]

        if (input_string[idx_1 - 1] == target) ^ (input_string[idx_2 - 1] == target):
            count = count + 1

    return count


def part_one(data):
    count = 0
    for line in data:
        sub = line.split()
        bounds = sub[0].split('-')

        lower = int(bounds[0])
        upper = int(bounds[1])

        target = sub[1].replace(':', '')

        input_string = sub[2]

        num_instances = input_string.count(target)

        if lower <= num_instances <= upper:
            count = count + 1
    return count


data = open('day02.txt', 'r').read().splitlines()

print(f'Part One: {part_one(data)}')
print(f'Part Two: {part_two(data)}')
