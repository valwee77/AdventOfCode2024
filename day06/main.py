def read_data():

    file_path = 'input.txt'
    map = []

    with open(file_path, 'r') as file:
        for line in file:
            map.append(list(line.strip()))

    return map

def find_guard(map):

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] not in ('.','#'): #finds position of guard
                return (i,j)
    return None

def direction(guard):

    if guard == "^":
        return -1,0
    elif guard == ">":
        return 0, 1
    elif guard == "v":
        return 1, 0
    else:
        return 0, -1

def change_direction(guard):
    if guard == "^":
        return ">"
    elif guard == ">":
        return "v"
    elif guard == "v":
        return "<"
    else:
        return "^"

def route(map):
    
    i,j = find_guard(map)

    while i < len(map):
        while j < len(map[i]):
            x, y = direction(map[i][j]) #find next coordinates

            new_i = i + x
            new_j = j + y

            if not (0 <= new_i < len(map) and 0 <= new_j < len(map[i])):
                map[i][j] = "X"
                return
            if map[new_i][new_j] == "#":
                guard = change_direction(map[i][j])
                map[i][j] = guard
                x, y = direction(map[i][j])
                new_i = i + x
                new_j = j + y

            map[new_i][new_j] = map[i][j]
            map[i][j] = "X"
            i = new_i
            j = new_j

def count_positions(map):

    count = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "X":
                count += 1
                
    return count

map = read_data()
route(map)
count = count_positions(map)
print(count)
