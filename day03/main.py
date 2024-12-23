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
    
    total = 0

    for eq in eqList:
        x, y = map(int, eq.split(','))
        total += multiply(x,y)

    return total

def solve_p1(line):
    eqList = clean_line(line)
    total = compute(eqList)
    return total

def solve_p2(line):
    begin = 0
    total = 0
    end = len(line)
    while True:
        start = line.find("do()", begin)
        stop = line.find("don't()", begin)
        if start == -1:
            if 0 < begin < stop:
                eqList = clean_line(line[begin:stop])
                total += compute(eqList)
            elif 0 < begin < end:
                eqList = clean_line(line[begin:end])
                total += compute(eqList)
            break
        elif stop == -1:
            if 0 < begin < end:
                eqList = clean_line(line[begin:end])
                total += compute(eqList)
            break

        if begin < last:
            eqList = clean_line(line[begin:last])
            total += compute(eqList)
        
        begin = start+1
    return total

line = read_line()
p1 = solve_p1(line)
p2 = solve_p2(line)
print(p2)