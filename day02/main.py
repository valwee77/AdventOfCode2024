def get_data():
    
    file_path = "input.txt"
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])

    return data

def check_safe(report):

    increasing = True
    decreasing = True

    for i in range(len(report)-1):
        diff = report[i + 1] - report[i]
        if 1 <= diff <= 3:  # Valid increase
            decreasing = False
        elif -3 <= diff <= -1:  # Valid decrease
            increasing = False
        else:  # Neither increasing nor decreasing
            return False

    return increasing or decreasing

def dampener(report):

    for i in range(len(report)):
        if check_safe(report[:i] + report[i+1:]):
            return True
    
    return False


def p1(data):

    count = 0

    for report in data:
        if check_safe(report):
            count += 1

    return count

def p2(data):

    count = 0

    for report in data:
        if dampener(report):
            count += 1

    return count

            


data = get_data()
p1 = p1(data)
p2 = p2(data)
print(p1)
print(p2)
