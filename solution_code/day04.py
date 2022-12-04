from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 4: Camp Cleanup
"""

puzzle = Puzzle(year=2022, day=4)

"""
Part A: 
Find the pair of elves for which one elf's cleaning assignment fully contains the other's
"""

def part_a(test=False):
    data = get_test_input('day04') if test else Puzzle(year=2022, day=4).input_data
    data = data.splitlines()
    data = [[[int(x) for x in section.split('-')] for section in line.split(',')] for line in data]
    return sum([1 if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]) else 0 for elf1, elf2 in data])

assert(part_a(test=True) == 2)
answer_a = part_a()
write_solution('day04', 'a', answer_a)
puzzle.answer_a = answer_a  

"""
Part B:
In how many assignment pairs do the ranges overlap?
"""

def part_b(test=False):
    data = get_test_input('day04') if test else Puzzle(year=2022, day=4).input_data
    data = data.splitlines()
    data = [[[int(x) for x in section.split('-')] for section in line.split(',')] for line in data]
    return sum([1 if len(set(range(elf1[0], elf1[1]+1)).intersection(set(range(elf2[0], elf2[1]+1)))) > 0 else 0 for elf1, elf2 in data])

assert(part_b(test=True) == 4)
answer_b = part_b()
write_solution('day04', 'b', answer_b)
puzzle.answer_b = answer_b