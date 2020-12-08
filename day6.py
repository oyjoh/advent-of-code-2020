def solve_part_two(data):
    total_sum = 0
    temp_list_of_sets = []
    temp_set = set([])
    for line in data:
        if line == '':
            total_sum += len(set(temp_list_of_sets[0]).intersection(*temp_list_of_sets))
            temp_list_of_sets = []
            continue
        temp_set = set([])
        for char in line:
            temp_set.add(char)
        temp_list_of_sets.append(temp_set)

    temp_list_of_sets.append(temp_set)
    total_sum += len(set(temp_list_of_sets[0]).intersection(*temp_list_of_sets))
    return total_sum


def solve_part_one(data):
    total_sum = 0
    temp_set = set([])
    for line in data:
        if line == '':
            total_sum += len(temp_set)
            temp_set = set([])
            continue
        for char in line:
            temp_set.add(char)

    total_sum += len(temp_set)
    return total_sum


def main():
    data = open('day6.txt', 'r').read().splitlines()
    print(f'Part One: {solve_part_one(data)}')
    print(f'Part Two: {solve_part_two(data)}')


main()
