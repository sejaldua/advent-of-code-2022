from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 7: The Treachery of Whales
"""

puzzle = Puzzle(year=2021, day=7)

def summation(n: int) -> int:
    return sum(range(1, n + 1))

def driver(test=False, constant_fuel_burn=True):
    data = get_test_input('day07') if test else Puzzle(year=2021, day=7).input_data
    positions = list(map(int,data.split(',')))
    if constant_fuel_burn:
        fuels = [sum(map(lambda x: abs(x - i), positions)) for i in range(max(positions)+1)]
    else:
        fuels = [sum(map(lambda x: summation(abs(x - i)), positions)) for i in range(max(positions)+1)]
    return min(fuels)

"""
Part A: 
Crabs aligning at one horizontal position given initial positions
Example:
Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel
Determine the horizontal position that the crabs can align to using the 
least fuel possible. How much fuel must they spend to align to that position?
"""

assert(driver(test=True) == 37)
answer_a = driver()
write_solution('day07', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
As it turns out, crab submarine engines don't burn fuel at a constant rate. 
Instead, each change of 1 step in horizontal position costs 1 more unit of 
fuel than the last: the first step costs 1, the second step costs 2, the 
third step costs 3, and so on... --> need to take sum of series
Example: 7 --> 2 = summation(5) = 1 + 2 + 3 + 4 + 5 = 15
Determine the horizontal position that the crabs can align to using the 
least fuel possible so they can make you an escape route! How much fuel 
must they spend to align to that position?
"""

assert(driver(test=True, constant_fuel_burn=False) == 168)
answer_b = driver(constant_fuel_burn=False)
write_solution('day07', 'b', answer_b)
# puzzle.answer_b = answer_b
