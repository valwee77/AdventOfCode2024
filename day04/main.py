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

def cross(crossword, find_word):

    x = int((len(find_word)-1)/2) # center index of find_word
    total = 0

    for i in range(x, len(crossword)-x):
        for j in range(x, len(crossword[0])-x):
            if crossword[i][j] == find_word[x]:
                letter = x
                while letter > 0:
                    d1 = [crossword[i-letter][j-letter], crossword[i+letter][j+letter]]
                    d2 = [crossword[i-letter][j+letter], crossword[i+letter][j-letter]]

                    if (d1 == [find_word[letter-1], find_word[letter+1]] or d1 == [find_word[letter+1], find_word[letter-1]]) \
                        and (d2 == [find_word[letter-1], find_word[letter+1]] or d2 == [find_word[letter+1], find_word[letter-1]]):
                        total += 1
                    letter -= 1

    return total

def p1(crossword, find_word):

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


p1_find_word = ["X", "M", "A", "S"]
p2_find_word = ["M", "A", "S"]
crossword = get_crossword()
p1 = p1(crossword, p1_find_word)
print("p1 =", p1)
p2 = cross(crossword, p2_find_word)
print("p2 =", p2)