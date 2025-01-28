def read_data():

    file_path = 'input.txt'
    map = []

    with open(file_path, 'r') as file:
        for line in file:
            map.append(list(line.strip()))

    return map

def direction(guard):

    if guard == "^":
        print("up")
        return 0,-1
    elif guard == "v":
        print("down")
    elif guard == ">":
        print("right")
    else:
        print("left")

def find_guard(map):

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] not in ('.','#'): #finds position of guard
                return (i,j)
    return None

def route(map):
    
    i=0 #stores current position of guard

    #find position of guard
    while i < len(map):
        j=0
        while j < len(map[i]):
            if map[i][j] not in ('.','#'): #finds position of guard
                x,y = direction(map[i][j])
                map[i+x][j+y] = map[i][j]
                map[i][j] = "x"
            j+=1
        i+=1
                



map = read_data()
route(map)
