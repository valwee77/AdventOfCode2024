def get_data():
    
    file_path = "input.txt"
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])

    return data

def solve_p1(data):
    
    increasing = True
    decreasing = True
    count = 0

    for report in data:
        for i in range(len(report)-1):
            if report[i] < report[i+1] and report[i+1] - report[i] <= 3:
                decreasing = False
            elif report[i] > report[i+1] and report[i] - report[i+1] <= 3:
                increasing = False
            else:
                increasing = False
                decreasing = False
        if increasing == True or decreasing == True:
            count += 1
        increasing = True
        decreasing = True
    return count



data = get_data()
count = solve_p1(data)
print(count)
