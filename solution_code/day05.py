from aocd.models import Puzzle
from utils import get_test_input, write_solution
from collections import defaultdict

"""
Day 5: Hydrothermal Venture
"""

puzzle = Puzzle(year=2021, day=5)

def str_to_tuple(coords: str) -> tuple:
    return tuple(map(int, coords.split(',')))

def parse_raw_data(data: list) -> list:
    lines = list(map(lambda x: x.split(" -> "), data.splitlines()))
    lines = list(map(lambda line: [str_to_tuple(coords) for coords in line], lines))
    return lines

def draw(grid: list, coords: list, ignore_diagonal: bool = False) -> list:
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[(x, y1)] += 1
    elif not ignore_diagonal and abs(x1 - x2) == abs(y1 - y2):
        dx = 1 if x1 < x2 else -1
        dy = 1 if y1 < y2 else -1
        for n in range(abs(x1 - x2) + 1):
            grid[(x1 + n * dx, y1 + n * dy)] += 1
    return grid

def driver(test=False, ignore_diagonal=True):
    data = get_test_input('day05') if test else Puzzle(year=2021, day=5).input_data
    all_lines = parse_raw_data(data)
    grid = defaultdict(int)
    for coords in all_lines:
        grid = draw(grid, coords, ignore_diagonal=ignore_diagonal)
    return sum(1 for vents in grid.values() if vents > 1)

"""
Part A: 
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 
where x1,y1 are the coordinates of one end the line segment and x2,y2 are the 
coordinates of the other end. These line segments include the points at both 
ends. 
Consider only horizontal and vertical lines (lines where either 
x1 = x2 or y1 = y2). At how many points do at least two lines overlap?  
"""

assert(driver(test=True, ignore_diagonal=True) == 5)
answer_a = driver(ignore_diagonal=True)
write_solution('day05', 'a', answer_a)
puzzle.answer_a = answer_a

"""
Part B: 
Consider all of the lines (including diagonals). At how many points 
do at least two lines overlap?
"""

assert(driver(test=True, ignore_diagonal=False) == 12)
answer_b = driver(ignore_diagonal=False)
write_solution('day05', 'b', answer_b)
puzzle.answer_b = answer_b
