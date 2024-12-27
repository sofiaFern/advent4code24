import csv

left_col, right_col = [], []
final_lst = []

# PART 1: choice of brute force :) 
with open('challenge_inputs/day1_input.csv', 'r') as file:
    reader = csv.reader(file)
    # csv_reader = csv.DictReader(file, delimiter="\t")
    for row in reader:
        hm = row[0].split(' ')
        left_col.append(hm[0])
        right_col.append(hm[3])

sorted_left_lst = sorted(left_col)
sorted_right_lst = sorted(right_col)

# NOTE - not worrying about lengths being different
for index, value in enumerate(sorted_left_lst):

    abs_val = abs(int(value) - int(sorted_right_lst[index]))
    final_lst.append(abs_val)

print(f'part 1 answer:  {sum(final_lst)}')

## PART 2 - Similarity List ## 
h_store = {}
similarity_lst = []
for left_val in sorted_left_lst:

    if left_val not in h_store:
        val_times = right_col.count(left_val)
        h_store[left_val] = val_times
    
    similarity_lst.append(int(left_val) * int(h_store[left_val]))

print(f'part 2 answer:  {sum(similarity_lst)}')