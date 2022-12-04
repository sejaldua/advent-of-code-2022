from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 3: Rucksack Reorganization
"""

puzzle = Puzzle(year=2022, day=3)

"""
Part A: 
Find the item that appears in both compartments of the rucksack
Then sum up the priority level of all items that appear in both compartments of their rucksack
"""

def get_priority(letter):
    return ord(letter) - ord('a') + 1 if letter.islower() else ord(letter) - ord('A') + 27

def part_a(test=False):
    data = get_test_input('day03') if test else Puzzle(year=2022, day=3).input_data
    data = data.splitlines()
    lengths = [round(len(line) / 2) for line in data]
    return sum([get_priority(list(set(list(line[:lengths[i]])).intersection(set(list(line[lengths[i]:]))))[0]) for i, line in enumerate(data)]) 

assert(part_a(test=True) == 157)
answer_a = part_a()
write_solution('day03', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
There is one common badge type in each group of 3 elves' rucksacks
Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
"""

def part_b(test=False):
    data = get_test_input('day03') if test else Puzzle(year=2022, day=3).input_data
    data = data.splitlines()
    groups = [data[n:n+3] for n in range(0, len(data), 3)]
    return sum([get_priority(list(set(list(line[0])).intersection(set(list(line[1]))).intersection(set(list(line[2]))))[0]) for line in groups])

assert(part_b(test=True) == 70)
answer_b = part_b()
write_solution('day03', 'b', answer_b)
puzzle.answer_b = answer_b