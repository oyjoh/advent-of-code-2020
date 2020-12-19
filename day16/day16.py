def solve_part_one(rules, nearby_tickets):
    valid_numbers = []
    invalid_numbers = []
    valid_tickets = []

    for rule in rules:
        arr = rule.split()
        range1 = arr[-3].split('-')
        range2 = arr[-1].split('-')
        valid_numbers += list(range(int(range1[0]), int(range1[1]) + 1))
        valid_numbers += list(range(int(range2[0]), int(range2[1]) + 1))

    for ticket in nearby_tickets:
        ticket = list(map(int, ticket.split(',')))
        valid = True
        for num in ticket:
            if num not in valid_numbers:
                invalid_numbers.append(num)
                valid = False
        if valid:
            valid_tickets.append(ticket)

    return sum(invalid_numbers), valid_tickets


def fit_rules(column, rules):
    valid_rules = []

    for idx, rule in enumerate(rules):
        passing = True
        for num in column:
            if num not in rule[0] and num not in rule[1]:
                passing = False
                break
        if passing:
            valid_rules.append(idx)

    return valid_rules


def create_rules(raw_rules):
    rules = []
    first_name = []
    for rule in raw_rules:
        arr = rule.split()
        first_name.append(arr[0])
        range1 = arr[-3].split('-')
        range2 = arr[-1].split('-')
        rules.append((range(int(range1[0]), int(range1[1]) + 1), range(int(range2[0]), int(range2[1]) + 1)))

    return rules, first_name


def pick_rule(column_valid_rules):
    already_used = []
    picked_rules = []
    num_assigned = 0

    for tup in column_valid_rules:
        for val in tup[1]:
            if val not in already_used:
                picked_rules.append((tup[0], val))
                already_used.append(val)
                num_assigned += 1
                break
    return picked_rules


def solve_part_two(rules, valid_nearby_tickets, my_ticket):
    columns = list(zip(*valid_nearby_tickets))
    column_valid_rules = []  # list of indexes of fitting rules

    rules, rule_name = create_rules(rules)

    for idx, column in enumerate(columns):
        column_valid_rules.append((idx, fit_rules(column, rules)))

    column_selected_rule = pick_rule(sorted(column_valid_rules, key=lambda x: len(x[1])))

    solution_sum = 1

    for tup in column_selected_rule:
        if rule_name[tup[1]] == 'departure':
            solution_sum *= my_ticket[tup[0]]

    return solution_sum


def main():
    data = open('day16.txt', 'r').read().split('\n\n')
    rules = data[0].splitlines()

    my_ticket = data[1].splitlines()[1]  # string
    my_ticket = list(map(int, my_ticket.split(',')))
    nearby_tickets = data[2].splitlines()[1:]

    sum_invalid, valid_nearby_tickets = solve_part_one(rules, nearby_tickets)
    print(f'Part One: {sum_invalid}')
    print(f'Part Two: {solve_part_two(rules, valid_nearby_tickets, my_ticket)}')


if __name__ == '__main__':
    main()
