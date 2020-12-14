import itertools


def apply_mask(val, mask):
    bin_val = list('{:036b}'.format(int(val)))

    for idx, char in enumerate(mask):
        if char == '0' or char == '1':
            bin_val[idx] = char

    result = int("".join(str(i) for i in bin_val), 2)

    return result


def solve_part_one(data):
    mem = {}
    mask = ''

    for line in data:
        sub = line.split()
        if sub[0] == 'mask':
            mask = sub[2]
            continue

        addr = int(sub[0][4:-1])
        val = sub[2]
        mem[addr] = apply_mask(val, mask)

    return sum(mem.values())


def get_addr(base_addr, mask):
    bin_addr = list('{:036b}'.format(int(base_addr)))

    for idx, char in enumerate(mask):
        if char == 'X' or char == '1':
            bin_addr[idx] = char

    num_floating = mask.count('X')
    lst = list(map(list, itertools.product([0, 1], repeat=num_floating)))

    addr_list = []
    for combination in lst:
        comb_idx = 0
        new_addr = bin_addr.copy()
        for idx, char in enumerate(new_addr):
            if char == 'X':
                new_addr[idx] = combination[comb_idx]
                comb_idx += 1
        addr_list.append(int("".join(str(i) for i in new_addr), 2))

    return addr_list


def solve_part_two(data):
    mem = {}
    mask = ''

    for line in data:
        sub = line.split()
        if sub[0] == 'mask':
            mask = sub[2]
            continue

        val = sub[2]
        base_addr = int(sub[0][4:-1])
        all_addr = get_addr(base_addr, mask)

        for addr in all_addr:
            mem[addr] = int(val)

    return sum(mem.values())


def main():
    data = open('day14.txt', 'r').read().splitlines()

    print(f'Part One: {solve_part_one(data)}')
    print(f'Part Two: {solve_part_two(data)}')


main()
