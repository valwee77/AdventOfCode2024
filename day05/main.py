from collections import defaultdict

def read_data():
    # seperates data into page ordering rules and page sets
    file_path = "input.txt"
    rules = defaultdict(list)
    page_set = []

    with open(file_path, 'r') as file:
        for line in file:

            line = line.strip()
            if not line:
                continue

            if "|" in line:
                x, y = map(int, line.split("|"))
                rules[x].append(y)
            else:
                page_set.append(list(map(int, line.strip().split(","))))

    return rules, page_set

def check_rule(rules, pages):
    #checks if pages are ordered correctly
    page_positions = {page: i for i, page in enumerate(pages)}
    for page in pages:
        for after in rules[page]:
            if after in page_positions and page_positions[after] < page_positions[page]:
                return False
    return True

def order_pages(rules, pages):
    #orders incorrectly ordered pages
    
    i = 0
    while i < len(pages):
        page = pages[i]
        page_positions = {page: i for i, page in enumerate(pages)}
        for after in rules[page]:
            if after in page_positions and page_positions[after] < page_positions[page]:
                pages[page_positions[page]], pages[page_positions[after]] = pages[page_positions[after]], pages[page_positions[page]]
                page_positions = {page: i for i, page in enumerate(pages)}
                i = page_positions[page]
        i += 1

    return pages


def check(rules, page_set):
    # sums up the middle pages for ordered pages and unordered pages
    ordered_total = 0
    unordered_total = 0
    for pages in page_set:
        if check_rule(rules, pages):
            middle = len(pages) // 2
            ordered_total += pages[middle]
        else:
            ordered_pages = order_pages(rules, pages)
            if check_rule(rules, ordered_pages):
                middle = len(ordered_pages) // 2
                unordered_total += ordered_pages[middle]


    return ordered_total, unordered_total

rules, page_set = read_data()
ordered_total, unordered_total = check(rules, page_set)
print(ordered_total, unordered_total)