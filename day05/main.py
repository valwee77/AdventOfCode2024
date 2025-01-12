from collections import defaultdict

def read_data():

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
    page_positions = {page: i for i, page in enumerate(pages)}
    for page in pages:
        for after in rules[page]:
            if after in page_positions and page_positions[after] < page_positions[page]:
                return False
    return True

def check_order(rules, page_set):
    total = 0
    for pages in page_set:
        if check_rule(rules, pages):
            middle = len(pages) // 2
            total += pages[middle]
    return total

rules, page_set = read_data()
total = check_order(rules, page_set)
print(total)