def get_crossword():
    
    #read input file and return the crossword puzzle in array format

    file_path = "input.txt"
    crossword = []

    with open(file_path, 'r') as file:
        for line in file:
            crossword.append(list(line.strip()))

    return crossword



crossword = get_crossword()