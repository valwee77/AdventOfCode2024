def read_line():

    file_path = 'input.txt'

    with open(file_path, 'r') as file:
        line = file.readline().strip()

    return line

def clean_line(line):
    begin = 0
    eqList = []
    eq = ''
    while True:
        start = line.find('mul(', begin)

        if start == -1:
            break

        end = line.find(')', start)

        eq = 'mul('
        for i in range(start + 4, end):
            char = line[i]
            if not (char.isdigit() or char == ',' or char == '-'):
                eq = ''
                break
            else:
                eq += char
                if i == end-1:
                    eq += ')'
        
        if eq:
            eqList.append(eq)

        begin = start + 4

    return 0

line = read_line()
eqList = clean_line(line)