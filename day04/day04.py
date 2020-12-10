def solve_part_one(password_set):
    counter = 0
    for item in password_set:
        if len(item) == 8:
            counter += 1
        elif len(item) == 7 and 'cid' not in item:
            counter += 1
    return counter


def solve(passport_set):
    counter = 0
    for item in passport_set:
        if len(item) == 8:
            if not int(item.get('byr')) >= 1920 or not int(item.get('byr')) <= 2002:
                continue
            if not int(item.get('iyr')) >= 2010 or not int(item.get('iyr')) <= 2020:
                continue
            if not int(item.get('eyr')) >= 2020 or not int(item.get('eyr')) <= 2030:
                continue

            height = item.get('hgt')
            height_measure = item.get('hgt')[-2:]
            if height_measure == 'in':
                new_str = height.replace(height_measure, '')
                if not int(new_str) >= 59 or not int(new_str) <= 76:
                    continue
            elif height_measure == 'cm':
                new_str = height.replace(height_measure, '')
                if not int(new_str) >= 150 or not int(new_str) <= 193:
                    continue
            else:
                continue

            if not item.get('hcl')[0] == '#':
                continue
            if not len(item.get('hcl')) == 7:
                continue

            char_set = {'a', 'b', 'c', 'd', 'e', 'f'}
            num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
            for c in item.get('hcl')[1:]:
                if c not in char_set or c not in num_set:
                    continue

            ecl_set = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            ecl_val = item.get('ecl')
            if not len(ecl_val) == 3 or ecl_val not in ecl_set:
                continue

            pid_val = item.get('pid')
            if not len(pid_val) == 9 or not pid_val.isnumeric():
                continue

            counter += 1
            continue
        elif len(item) == 7:
            if 'cid' not in item:
                if not int(item.get('byr')) >= 1920 or not int(item.get('byr')) <= 2002:
                    continue
                if not int(item.get('iyr')) >= 2010 or not int(item.get('iyr')) <= 2020:
                    continue
                if not int(item.get('eyr')) >= 2020 or not int(item.get('eyr')) <= 2030:
                    continue

                height = item.get('hgt')
                height_measure = item.get('hgt')[-2:]
                if height_measure == 'in':
                    new_str = height.replace(height_measure, '')
                    if not int(new_str) >= 59 or not int(new_str) <= 76:
                        continue
                elif height_measure == 'cm':
                    new_str = height.replace(height_measure, '')
                    if not int(new_str) >= 150 or not int(new_str) <= 193:
                        continue
                else:
                    continue

                if not item.get('hcl')[0] == '#':
                    continue
                if not len(item.get('hcl')) == 7:
                    continue
                if not all(c.isdigit() or c.islower() for c in item.get('hcl')[1:]):  ## not a-f
                    continue

                char_set = set(['a', 'b', 'c', 'd', 'e', 'f'])
                num_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                for c in item.get('hcl')[1:]:
                    if c not in char_set or c not in num_set:
                        continue

                ecl_set = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                ecl_val = item.get('ecl')
                if not len(ecl_val) == 3 or ecl_val not in ecl_set:
                    continue

                pid_val = item.get('pid')
                if not len(pid_val) == 9 or not pid_val.isnumeric():
                    continue

                counter += 1
                continue
    return counter


data = open('day04.txt', 'r').read().splitlines()

passports = []
temp_set = {}

for line in data:
    if line == '':
        passports.append(temp_set)
        temp_set = {}
        continue

    sub = line.split(' ')
    for entry in sub:
        values = entry.split(':')
        temp_set[values[0]] = values[1]
passports.append(temp_set)

print(f'Part One: {solve_part_one(passports)}')
print(f'Part Two: {solve(passports)}')
