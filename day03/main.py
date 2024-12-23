def read_line():

    file_path = 'input.txt'

    with open(file_path, 'r') as file:
        line = file.read().replace('\n', '')

    return line

def clean_line(line):
    begin = 0
    eqList = []
    while True:
        start = line.find('mul(', begin)
        end = line.find(')', start)

        if start == -1:
            break

        eq = ''
        for i in range(start + 4, end):
            char = line[i]
            if not (char.isdigit() or char == ','):
                eq = ''
                break
            else:
                eq += char
        
        if eq:
            eqList.append(eq)

        begin = start + 4

    return eqList

def multiply(x,y):
    return x * y

def compute(eqList):
    
    sum = 0

    for eq in eqList:
        x, y = map(int, eq.split(','))
        sum += multiply(x,y)

    return sum

def solve_p1(line):
    eqList = clean_line(line)
    total = compute(eqList)
    return total

def solve_p2(line):
    return 0 

line = read_line()
p1 = solve_p1(line)
p2 = solve_p2(line)
print(p1)