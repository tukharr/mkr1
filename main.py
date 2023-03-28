def same(file1, file2):
    same_lines = []

    for line in file1:
        if line in file2:
            same_lines.append(line)

    with open("same.txt", 'w') as file:
        file.write("".join(same_lines))


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    return lines


def main():
    pass


if __name__ == '__main__':
    main()
