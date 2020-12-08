def num_shiny_children(bag_list, bag_dict):
    counter = 0
    for bag in bag_list:
        if bag[1:] == 'shinygold':
            return 1
        else:
            counter += num_shiny_children(bag_dict[bag[1:]], bag_dict)

    return counter


def child_counter(bag_list, bag_dict):
    bag_count = 0
    for bag in bag_list:
        num_bag = bag[0]
        bag_type = bag[1:]

        for i in range(int(num_bag)):
            bag_count += 1
            bag_count += child_counter(bag_dict[bag_type], bag_dict)
    return bag_count


def solve_part_one(bag_dict):
    shiny_counter = 0
    for x in bag_dict:
        if x == 'shinygold':
            continue
        if num_shiny_children(bag_dict[x], bag_dict) > 0:
            shiny_counter += 1
    return shiny_counter


def solve_part_two(bag_dict):
    return child_counter(bag_dict['shinygold'], bag_dict)


bag_dict = {}

data = open('day7.txt', 'r').read().splitlines()

for line in data:
    string_arr = line.split()

    parent_bag = string_arr[0] + string_arr[1]
    bag_dict[parent_bag] = []
    if len(string_arr) == 7:
        continue

    num_children = int((len(string_arr) - 4) / 4)

    for i in range(5, len(string_arr), 4):
        bag_name = string_arr[i - 1] + string_arr[i] + string_arr[i + 1]
        bag_dict[parent_bag].append(bag_name)


print(f'Part One: {solve_part_one(bag_dict)}')
print(f'Part Two: {solve_part_two(bag_dict)}')
