import operator

ops = {'+': operator.add, '-': operator.sub}


def get_loop_acc(data_inp):
    data_cp = data_inp.copy()
    acc_val = 0
    instruction_idx = 0
    loop_detected = False

    while not loop_detected and instruction_idx < len(data_cp):
        if data_cp[instruction_idx] == 'visited':
            loop_detected = True
            break

        instruction = data_cp[instruction_idx].split()

        operator = instruction[1][:1]
        val = instruction[1][1:]

        if instruction[0] == 'acc':
            acc_val = ops[operator](acc_val, int(val))
            data_cp[instruction_idx] = 'visited'
            instruction_idx += 1
        elif instruction[0] == 'nop':
            data_cp[instruction_idx] = 'visited'
            instruction_idx += 1
        elif instruction[0] == 'jmp':
            data_cp[instruction_idx] = 'visited'
            instruction_idx = ops[operator](instruction_idx, int(val))
    return loop_detected, acc_val


def solve_part_two(data):
    flip_table = {'nop': 'jmp', 'jmp': 'nop'}
    non_loop_acc = -1
    for idx, line in enumerate(data):
        instruction = line.split()
        if instruction[0] == 'nop' or instruction[0] == 'jmp':
            orig = data[idx]
            data[idx] = flip_table[instruction[0]] + ' ' + instruction[1]
            loop, acc = get_loop_acc(data)
            if not loop:
                non_loop_acc = acc
                break
            else:
                data[idx] = orig
    return non_loop_acc


def main():
    data = open('day8.txt', 'r').read().splitlines()

    print(f'Part One: {get_loop_acc(data)[1]}')
    print(f'Part Two: {solve_part_two(data)}')


main()
