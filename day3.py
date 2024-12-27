import re
import csv

# PART 1 #
with open('challenge_inputs/day3_input.csv', 'r') as file:
    input_string = file.read()

# Part 1
pattern = r"mul\((\d+),(\d+)\)"
# matches = re.findall(pattern, input_string)
# total_sum = sum(int(x) * int(y) for x, y in matches)
# print(f'total_sum of mul(x,y) {total_sum}')

# Part 2 - slack advent of code
input = input_string.split('do()')
input = ''.join([d.split("don't()")[0] for d in input])
total_mult = sum([int(mult[4:-1].split(',')[0]) * int(mult[4:-1].split(',')[1]) for mult in re.findall(pattern, input)])

print(total_mult)