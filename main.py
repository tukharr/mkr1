def same(file1, file2):
    file1_lines = read_file(file1)
    file2_lines = read_file(file2)
    same_lines = []

    for line in file1_lines:
        if line in file2_lines:
            same_lines.append(line)

    with open("same.txt", 'w') as file:
        file.write("".join(same_lines))

    return same_lines


def diff(file1, file2):
    file1_lines = read_file(file1)
    file2_lines = read_file(file2)

    different_lines = []
    all_lines = file2_lines.copy()

    for line in file1_lines:
        if line not in file2_lines:
            all_lines.append(line)

    for line in all_lines:
        if line not in file2_lines or line not in file1_lines:
            different_lines.append(line)

    with open("diff.txt", 'w') as file:
        file.write("".join(different_lines))

    return different_lines


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    return lines


if __name__ == '__main__':
    pass
