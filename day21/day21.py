def solve_part_one(data):
    master_dict = {}
    master_ingredients = []

    for line in data:
        allergens = line[line.find('(') + 10: line.find(')')].split(', ')
        ingredients = line[:line.find('(')].split()
        master_ingredients += ingredients

        for a in allergens:
            if a not in master_dict.keys():
                master_dict[a] = []
            master_dict[a].append(set(ingredients.copy()))

    core = set([])

    for val in master_dict.values():
        allergens_set = set.intersection(*val)
        for v in allergens_set:
            core.add(v)

    counter = 0

    for i in master_ingredients:
        if i not in core:
            counter += 1
    return counter, master_dict


def remove_val_dict(param, new_dict):
    for key in new_dict:
        if param in new_dict[key]:
            new_dict[key].remove(param)
    return new_dict


def solve_part_two(master_dict):
    for key in master_dict:
        master_dict[key] = set.intersection(*master_dict[key])
    new_dict = dict(sorted(master_dict.items(), key=lambda item: len(item[1])))

    sol = {}
    while True:
        if len(new_dict) == 0:
            break
        for key in new_dict:
            if len(new_dict[key]) == 1:
                sol[key] = new_dict.pop(key).pop()
                new_dict = remove_val_dict(sol[key], new_dict)
                break

    result = []
    for key in sorted(sol.keys()):
        result.append(sol[key])

    return ','.join(result)


def main():
    data = open('day21.txt', 'r').read().splitlines()

    part_one_ans, master_dict = solve_part_one(data)
    print(f'Part One: {part_one_ans}')
    print(f'Part Two: {solve_part_two(master_dict)}')


if __name__ == '__main__':
    main()
