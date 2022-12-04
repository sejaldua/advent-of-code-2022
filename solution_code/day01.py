from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 1: Calorie Counting
"""

puzzle = Puzzle(year=2022, day=1)

"""
Part A: 
Count the number of calories each elf is carrying and find the elf carrying the most calories
"""

def part_a(test=False):
    data = get_test_input('day01') if test else Puzzle(year=2022, day=1).input_data
    elves = data.split("\n\n")
    nums = [sum([int(n) for n in x.split("\n")]) for x in elves]
    return max(nums)

assert(part_a(test=True) == 24000)
answer_a = part_a()
write_solution('day01', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
Get the sum of the top 3 elves carrying the most calories
"""

def part_b(test=False):
    data = get_test_input('day01') if test else Puzzle(year=2022, day=1).input_data
    elves = data.split("\n\n")
    nums = sorted([sum([int(n) for n in x.split("\n")]) for x in elves], reverse=True)
    return sum(nums[:3])

assert(part_b(test=True) == 45000)
answer_b = part_b()
write_solution('day01', 'b', answer_b)
puzzle.answer_b = answer_b