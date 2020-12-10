def solve_part_one(data):
    one_diff_count = 0
    three_diff_count = 0

    for i in range(1, len(data)):
        if data[i] - data[i - 1] == 1:
            one_diff_count += 1
        else:
            three_diff_count += 1
    return one_diff_count * three_diff_count


def solve_part_two(data, memo, root_idx):
    root = data[root_idx]
    endpoints = 0

    if memo[root_idx] != -1:
        return memo[root_idx]

    if root_idx + 1 == len(data):
        endpoints += 1

    for i in range(root_idx + 1, len(data)):
        if data[i] - root <= 3:
            child_endpoints = solve_part_two(data, memo, i)
            endpoints += child_endpoints
            memo[i] = child_endpoints
        else:
            break
    return endpoints


def main():
    data = open('day10.txt', 'r').read().splitlines()
    data = list(map(int, data))

    data.append(max(data) + 3)
    data.append(0)
    data.sort()

    print(f'Part One: {solve_part_one(data)}')
    print(f'Part Two: {solve_part_two(data, [-1] * len(data), 0)}')


main()
