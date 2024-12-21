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

def check_safe(report):

    increasing = True
    decreasing = True

    for i in range(len(report)-1):
        if report[i] < report[i+1] and report[i+1] - report[i] <= 3:
            decreasing = False
        elif report[i] > report[i+1] and report[i] - report[i+1] <= 3:
            increasing = False
        else:
            increasing = False
            decreasing = False
    if increasing == True or decreasing == True:
        return True

    return False

def dampener(data):

    count = 0

    for report in data:
        for i in range(len(report)):
            if check_safe(report[:i] + report[i+1:]):
                count += 1
                break
    
    return count
            


data = get_data()
solve_p1(data)
count = dampener(data)
print(count)




"""
    increasing = 0
    decreasing = 0
    count = 0

    for report in data:
        for i in range(len(report)-1):
            if report[i] < report[i+1] and report[i+1] - report[i] <= 3:
                increasing += 1
            elif report[i] > report[i+1] and report[i] - report[i+1] <= 3:
                decreasing += 1
            elif i+2 < len(report):
                if report[i] < report[i+2] and report[i+2] - report[i] <= 3:
                    increasing += 1
                elif report[i] > report[i+2] and report[i] - report[i+2] <= 3:
                    decreasing += 1
        if (increasing+decreasing) >= len(report)-1:
            count += 1
        increasing = 0 
        decreasing = 0
    return count
"""


"""try 2
count = 0

    for report in data:

        i=1
        dampen = 0
        increase = False
        decrease = False

        while i < len(report)-1:
            
            incA = report[i] - report[i-1]
            incB = report[i+1] - report[i]
            decA = report[i-1] - report[i]
            decB = report[i] - report[i+1]

            if 0<incA<=3 and 0<incB<=3:
                increase = True
                i += 1
            elif 0<decA<=3 and 0<decB<=3:
                decrease = True
                i += 1
            elif dampen == 0:
                report.pop(i)
                dampen += 1
            else:
                decrease = False
                increase = False
                break

        if dampen <= 1 and increase == True and decrease == False:
            count += 1 
        elif dampen <=1 and increase == False and decrease == True:
            count += 1
"""