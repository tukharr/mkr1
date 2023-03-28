def same(file1, file2):
    same_lines = []

    for line in file1:
        if line in file2:
            same_lines.append(line)

    with open("same.txt", 'w') as file:
        file.write("".join(same_lines))


def diff(file1, file2):
    different_lines = []
    all_lines = file2.copy()

    for line in file1:
        if line not in file2:
            all_lines.append(line)

    for line in all_lines:
        if line not in file2 or line not in file1:
            different_lines.append(line)

    with open("diff.txt", 'w') as file:
        file.write("".join(different_lines))


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    return lines


def main():
    pass


if __name__ == '__main__':
    main()
