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
    for page in pages[::-1]:
        test = rules[page]
        print(test)


def check_order(rules, page_set):
    for pages in page_set:
        check_rule(rules, pages)


rules, page_set = read_data()
check_order(rules, page_set)