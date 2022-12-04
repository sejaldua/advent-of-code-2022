from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 1: Sonar Sweep
"""

puzzle = Puzzle(year=2021, day=1)

"""
Part A: 
Count the number of times a depth measurement increases from the previous measurement. How many measurements are larger than the previous measurement?

    199 (N/A - no previous measurement)
    200 (increased)
    208 (increased)
    210 (increased)
    200 (decreased)
    207 (increased)
    240 (increased)
    269 (increased)
    260 (decreased)
    263 (increased)
"""

def part_a(test=False):
    data = get_test_input('day01') if test else Puzzle(year=2021, day=1).input_data
    nums = [int(n) for n in data.splitlines()]
    answer_a = sum([1 if nums[i] > nums[i-1] else 0 for i in range(1, len(nums))])
    return answer_a

assert(part_a(test=True) == 7)
answer_a = part_a()
write_solution('day01', 'a', answer_a)
# puzzle.answer_a = answer_a  


"""
Part B:
Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
"""

def part_b(test=False):
    data = get_test_input('day01') if test else Puzzle(year=2021, day=1).input_data
    nums = [int(n) for n in data.splitlines()]
    answer_b = sum([1 if sum(nums[i:i+3]) > sum(nums[i-1:i+2]) else 0 for i in range(1, len(nums)-2)])
    return answer_b

assert(part_b(test=True) == 5)
answer_b = part_b()
write_solution('day01', 'b', answer_b)
# puzzle.answer_b = answer_b