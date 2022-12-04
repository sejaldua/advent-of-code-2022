from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 6: Lanternfish
"""

puzzle = Puzzle(year=2021, day=6)

# non-optimized version
def exponential_lanternfish(days, test=False):
    data = get_test_input('day06') if test else Puzzle(year=2021, day=6).input_data
    timers = list(map(int, data.split(',')))
    for _ in range(days):
        num_new_fish = timers.count(0)
        timers = [val - 1 if val != 0 else 6 for val in timers] + ([8] * num_new_fish)
    return len(timers)

# recursive function
def pass_time(fertility: list, days: int) -> list:
    if days == 0:
        return sum(fertility)
    
    fertility = [
        # Timers 1-6 are mapped to 0-5 respectively.
        *[fertility[n] for n in range(1, 7)],
        # Timers 0 and 7 are mapped to 6.
        fertility[0] + fertility[7],
        # Timer 8 is mapped to 7.
        fertility[8],
        # Timer 0 is mapped to 8.
        fertility[0],
    ]
    return pass_time(fertility, days - 1)
            
def lanternfish(days, test=False):
    data = get_test_input('day06') if test else Puzzle(year=2021, day=6).input_data
    initial_timers = list(map(int, data.split(',')))
    fertility = [0] * 9
    for timer in initial_timers:
        fertility[timer] += 1
    num_fish = pass_time(fertility, days)
    return num_fish

"""
Part A: 
A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 
is included as a valid timer value). The new lanternfish starts with an 
internal timer of 8 and does not start counting down until the next day.

Example:
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8

Find a way to simulate lanternfish. How many lanternfish would there be 
after 80 days?
"""

assert(exponential_lanternfish(18, test=True) == 26)
assert(exponential_lanternfish(80, test=True) == 5934)
assert(lanternfish(18, test=True) == 26)
assert(lanternfish(80, test=True) == 5934)
answer_a = lanternfish(80)
write_solution('day06', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
How many lanternfish would there be after 256 days?
This part is testing how well the code scales... will face issues
if exponential Big-O.
"""

assert(lanternfish(256, test=True) == 26984457539)
answer_b = lanternfish(256)
write_solution('day06', 'b', answer_b)
# puzzle.answer_b = answer_b
