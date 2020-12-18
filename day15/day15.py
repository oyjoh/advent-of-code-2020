def idx_diff(spoken_list):
    target = len(spoken_list)
    last = (len(spoken_list[:-1]) - 1 - spoken_list[:-1][::-1].index(spoken_list[-1])) + 1
    return target - last


def solve_part_one(data):
    spoken_list = data.copy()
    res_len = 0

    part_one = 2020

    while res_len < part_one:
        if spoken_list[:-1].count(spoken_list[-1]) == 0:
            spoken_list.append(0)
        else:
            spoken_list.append(idx_diff(spoken_list))
        res_len += 1

    return spoken_list[part_one - 1]


def solve_part_two(data):
    spoken_dict = {}

    for idx, number in enumerate(data[:-1]):
        spoken_dict[number] = idx + 1

    index = len(data)
    spoken_number = data[-1]

    while index < 30000000:
        if spoken_number not in spoken_dict.keys():
            spoken_dict[spoken_number] = index
            spoken_number = 0
        else:
            new_spoken = index - spoken_dict[spoken_number]
            spoken_dict[spoken_number] = index
            spoken_number = new_spoken
        index += 1

    return spoken_number


def main():
    data = open('day15.txt', 'r').read()
    data_arr = data.split(',')
    data_arr = list(map(int, data_arr))

    print(f'Part One: {solve_part_one(data_arr)}')
    print(f'Part Two: {solve_part_two(data_arr)}')


if __name__ == '__main__':
    main()
