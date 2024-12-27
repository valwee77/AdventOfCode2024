def get_crossword():
    
    #read input file and return the crossword puzzle in array format

    file_path = "input.txt"
    crossword = []

    with open(file_path, 'r') as file:
        for line in file:
            crossword.append(list(line.strip()))

    return crossword

def horizontal(crossword, find_word):

    # count number of times word appears horizontally

    letter = 0
    total = 0

    for i in range(len(crossword)):
        for j in range(len(crossword[0])-len(find_word)+1):
            match = True
            for letter in range(len(find_word)):
                if crossword[i][j+letter] != find_word[letter]:
                    match = False
                    break
            if match:
                total += 1

    return total

def vertical(crossword, find_word):

    # count number of times word appears vertically

    letter = 0
    total = 0
    
    for j in range(len(crossword[0])):
        for i in range(len(crossword) - len(find_word)+1):
            match = True
            for letter in range(len(find_word)):
                if crossword[i + letter][j] != find_word[letter]:
                    match = False
                    break
            if match:
                total += 1

    return total

def diagonal_right(crossword, find_word):

    # count number of times word appears diagonally to the right
    letter = 0
    total = 0

    for i in range(len(crossword)-len(find_word)+1):
        for j in range(len(crossword[0])-len(find_word)+1):
            match = True
            for letter in range(len(find_word)):
                if crossword[i+letter][j+letter] != find_word[letter]:
                    match = False
                    break
            if match:
                total += 1
    return total

def diagonal_left(crossword, find_word):

    # count number of times word appears diagonally down to the left

    letter = 0
    total = 0

    for i in range(len(find_word)-1, len(crossword)):
        for j in range(len(crossword[0])-len(find_word)+1):
            match = True
            for letter in range(len(find_word)):
                if crossword[i-letter][j+letter] != find_word[letter]:
                    match = False
                    break
            if match:
                total += 1
    return total

def sum(crossword, find_word):

    # sum of times a word appears in a crossword

    total = 0

    total += horizontal(crossword, find_word)
    total += horizontal(crossword, find_word[::-1])
    total += vertical(crossword, find_word)
    total += vertical(crossword, find_word[::-1])
    total += diagonal_right(crossword, find_word)
    total += diagonal_right(crossword, find_word[::-1])
    total += diagonal_left(crossword, find_word)
    total += diagonal_left(crossword, find_word[::-1])

    return total


find_word = ["X", "M", "A", "S"]
crossword = get_crossword()
total = sum(crossword, find_word)
print("total =", total)