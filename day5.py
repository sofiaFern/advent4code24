import csv

with open('challenge_inputs/day5_input.csv', 'r') as file:
    reader = csv.reader(file)
    page_store = {}
    rows = []

    for row in reader:
        print(row)
        if len(row) == 0:
            continue
        elif '|' in row[0]:
            first_page, second_page = row[0].split('|')
            page_store.setdefault(first_page, []).append(second_page)
        else: 
            rows.append(row)

def get_middle_item(lst):
    if not lst:
        return None
    middle_index = len(lst) // 2
    return lst[middle_index]

# PART 1: brute force :) 
successful_ordering = []

for row in rows:
    success = True
    for i, curr_val in enumerate(row):
        if curr_val not in page_store:
            continue
        elif i != 0 and any(item in row[:i] for item in page_store[curr_val]):
            success = False
            break
    if success:
        successful_ordering.append(row)

print(successful_ordering)

middle_items_sum = sum(int(get_middle_item(row)) for row in successful_ordering if get_middle_item(row) is not None)

print(middle_items_sum)