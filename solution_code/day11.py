from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 11: Dumbo Octopus
"""

puzzle = Puzzle(year=2021, day=11)

def neighbor_indices(matrix: np.ndarray, row: int, col: int):
    for dy in -1, 0, 1:
        for dx in -1, 0, 1:
            row_new = row + dy
            col_new = col + dx
            if row == row_new and col == col_new:
                continue
            if (0 <= row_new < matrix.shape[0]) and (0 <= col_new < matrix.shape[1]):
                yield row_new, col_new

def stepper(matrix):
    matrix += 1
    while (matrix > 9).any():
        for row, col in np.ndindex(*matrix.shape):
            if matrix[row, col] > 9:
                matrix[row, col] = 0
                for row_nbr, col_nbr in neighbor_indices(matrix, row, col):
                    if matrix[row_nbr, col_nbr] != 0:
                        matrix[row_nbr, col_nbr] += 1
    n_flashes = np.sum(matrix == 0)
    return matrix, n_flashes

"""
Part A: 
- There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus 
  slowly gains energy over time and flashes brightly for a moment when its 
  energy is full.
- You can model the energy levels and flashes of light in steps. During a
  single step, the following occurs:
  - First, the energy level of each octopus increases by 1.
  - Then, any octopus with an energy level greater than 9 flashes. 
    This increases the energy level of all adjacent octopuses by 1, including 
    octopuses that are diagonally adjacent. If this causes an octopus to have 
    an energy level greater than 9, it also flashes. This process continues as
    long as new octopuses keep having their energy level increased beyond 9. 
    (An octopus can only flash at most once per step.)
  - Finally, any octopus that flashed during this step has its energy level 
    set to 0, as it used all of its energy to flash.
Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?
"""

def part_a(n_steps: int, test: bool = False) -> int:
    data = get_test_input('day11') if test else Puzzle(year=2021, day=11).input_data
    matrix = np.array([[int(char) for char in line] for line in data.splitlines()])
    total_flashes = 0
    for _ in range(n_steps):
        matrix, n_flashes = stepper(matrix)
        total_flashes += n_flashes
    return total_flashes
    

assert(part_a(100, test=True) == 1656)
answer_a = part_a(100)
write_solution('day11', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
What is the first step during which all octopuses flash?
"""

def part_b(test: bool = False) -> int:
    data = get_test_input('day11') if test else Puzzle(year=2021, day=11).input_data
    matrix = np.array([[int(char) for char in line] for line in data.splitlines()])
    n_steps = 0
    while True:
        n_steps += 1
        matrix, n_flashes = stepper(matrix)
        if (n_flashes) == 100:
            return n_steps

assert(part_b(test=True) == 195)
answer_b = part_b()
write_solution('day11', 'b', answer_b)
# puzzle.answer_b = answer_b