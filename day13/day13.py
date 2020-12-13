from functools import reduce


# source: rosettacode
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


# source: rosettacode
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def solve_part_two(bus_list):
    mod_list_n = []
    mod_list_a = []
    subtract = 0

    for bus in bus_list:
        if bus == 'x':
            subtract += 1
            continue
        bus = int(bus)

        mod_list_n.append(bus - subtract)
        mod_list_a.append(bus)
        subtract += 1

    return chinese_remainder(mod_list_a, mod_list_n)


def solve_part_one(departure, bus_list):
    best_dep = departure
    best_id = -1

    for bus in bus_list:
        if bus == 'x':
            continue
        bus = int(bus)

        bus_factor = int(departure / bus)
        bus_dep = (bus_factor * bus) + bus
        bus_diff = bus_dep - departure

        if bus_diff < best_dep:
            best_dep = bus_diff
            best_id = bus
    return best_dep * best_id


def main():
    data = open('day13.txt', 'r').read().splitlines()
    departure = int(data[0])
    bus_list = data[1].split(',')

    print(f'Part One: {solve_part_one(departure, bus_list)}')
    print(f'Part Two: {solve_part_two(bus_list)}')


main()
