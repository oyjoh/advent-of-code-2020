def solve_part_one(data):
    master_dict = {}
    master_igr = []

    for line in data:
        allergens = line[line.find('(') + 10: line.find(')')].split(', ')
        ingredients = line[:line.find('(')].split()
        master_igr += ingredients

        for a in allergens:
            if a not in master_dict.keys():
                master_dict[a] = []
            master_dict[a].append(set(ingredients.copy()))

        # print(ingredients, end=' --> ')
        # print(allergens)

    core = set([])

    for val in master_dict.values():
        allger_set = set.intersection(*val)
        for val in allger_set:
            core.add(val)

    counter = 0
    for i in master_igr:
        if i not in core:
            counter += 1
    return counter


def main():
    data = open('day21.txt', 'r').read().splitlines()

    print(f'Part One: {solve_part_one(data)}')


def demo():
    x = {1, 2, 3}
    y = {0, 2, 3}
    k = {2, 0, 4}
    l = [x, y, k]
    z = x.intersection(y)
    sd = set.intersection(*l)
    # a = x.symmetric_difference(sam)

    ee = (x ^ y ^ k)
    print(sd)
    # print(ee)
    # print(a)


if __name__ == '__main__':
    main()
