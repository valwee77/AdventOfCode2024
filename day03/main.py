def read_line():

    # read input file and output a single line
    # output: single line of corrupted data

    file_path = 'input.txt'

    with open(file_path, 'r') as file:
        line = file.read().replace('\n', '')

    return line

def clean_line(line):

    # extract relevant equations from a corrupted line
    # input: corrupted line
    # output: list of "x,y" where x and y are numbers to be multiplied together

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
            # if character in 'mul()' is not a number or not a comma, exit loop and empty eq
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
    
    # finds the sum of all the multiplied numbers
    # input: list of "x,y" where x and y are numbers to be multiplied together
    # output: total of multiplied numbers

    total = 0

    for eq in eqList:
        x, y = map(int, eq.split(','))
        total += multiply(x,y)

    return total

def solve_p1(line):
    eqList = clean_line(line)
    return compute(eqList)

def solve_p2(line):

    # find do()s and don't()s. when do(), compute multiplications. when don't(), do not compute multiplications.

    enabled = True
    temp = ''
        
    for i in range(len(line)):
        if line[i:i+4] == "do()":
            enabled = True
        if line[i:i+7] == "don't()":
            enabled = False

        if enabled:
            temp += line[i]
            
    eqList = clean_line(temp)

    return compute(eqList) 

line = read_line()
p1 = solve_p1(line)
p2 = solve_p2(line)
print(p1)
print(p2)
