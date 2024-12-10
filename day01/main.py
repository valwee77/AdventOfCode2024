from collections import Counter

def get_lists():

    #1. read input file and split lines into 2 arrays

    file_path = "input.txt"
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def get_distance(left_list, right_list):

    #2. sort arrays
    
    distance = 0

    left_list.sort()
    right_list.sort()

    for i in range(max(len(left_list), len(right_list))):
        big = max(right_list[i], left_list[i])
        small = min(right_list[i], left_list[i])
        distance += (big - small)

    return distance


def get_score(left_list, right_list):

    #3. count items in right list

    score = 0
    counter = Counter(right_list)

    for i in left_list:
        if i in counter:
            score += (i * counter[i])
    return score


left, right = get_lists()
distance = get_distance(left, right)
score = get_score(left, right)
print(distance)
print(score)
