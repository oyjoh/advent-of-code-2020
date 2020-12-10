def is_sum_of_two(lst, num):
    for x in lst:
        for y in lst:
            if x + y == num and lst.index(x) != lst.index(y):
                return True
    return False


def get_first_error(data, len_preamble):
    preamble = data[:len_preamble]
    for i in range(len_preamble, len(data)):
        if not is_sum_of_two(preamble, data[i]):
            return data[i]
        else:
            preamble.append(data[i])
            preamble.pop(0)
    return -1


def find_seq(data, num):
    for i in range(2, 20):
        queue = data[:i]
        for k in range(i, len(data)):
            if sum(queue) == num:
                return max(queue) + min(queue)
            else:
                queue.append(data[k])
                queue.pop(0)
    return -1


def main():
    data = open('day09.txt', 'r').read().splitlines()
    data = list(map(int, data))
    print(f'Part One: {get_first_error(data, 25)}')
    print(f'Part Two: {find_seq(data, get_first_error(data, 25))}')


main()
