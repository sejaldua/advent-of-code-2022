from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 13: Transparent Origami
"""

puzzle = Puzzle(year=2021, day=13)

def get_unfolded_dot_paper(lines: list) -> np.ndarray:
    """ Construct the unfolded dot paper given dot coordinates """
    
    coords = [tuple(map(int, line.split(','))) for line in lines if ',' in line]
    folds = [tuple(line.strip('fold along ').split('=')) for line in lines if 'fold along' in line]
    folds = list(map(lambda x: (x[0], int(x[1])), folds))
    x_vals = set([tup[0] for tup in coords])
    y_vals = set([tup[1] for tup in coords])
    grid = np.zeros(shape=(max(y_vals)+1, max(x_vals)+1))
    for j, i in coords:
        grid[i][j] = 1
    return grid, folds

def perform_fold(grid, axis, index):
    """ 
    Perform a fold by merging both halves of the grid via numpy sum and
    flip operations
    """
    
    if axis == 'y':
        new_grid = grid[:index, :] + np.flipud(grid[index+1:, :])
    else:
        new_grid = grid[:, :index] + np.fliplr(grid[:, index+1:])
    return new_grid
    
def driver(test: bool=False, one_fold: bool=True) -> int:
    """ 
    Driver which works for Part A and B, only arg to flip is one_fold,
    which indicates whether to execute only one fold or all folds
    """
    
    data = get_test_input('day13').splitlines() if test else Puzzle(year=2021, day=13).input_data.splitlines()
    grid, folds = get_unfolded_dot_paper(data)
    for fold in folds:
        grid = perform_fold(grid, *fold)
        if one_fold:
            return np.sum(grid != 0)
    answer_str = "\n".join(["".join(list(map(lambda x: "#" if x > 0 else " ", line))) for line in grid.tolist()])
    return answer_str

"""
Part A:
- The first section is a list of dots on the transparent paper. 0,0 represents 
  the top-left coordinate. The first value, x, increases to the right. The 
  second value, y, increases downward.
- Then, there is a list of fold instructions. Each instruction indicates a line
  on the transparent paper and wants you to fold the paper up (for horizontal 
  y=... lines) or left (for vertical x=... lines).
- Also notice that some dots can end up overlapping; in this case, the dots 
  merge together and become a single dot.
How many dots are visible after completing just the first fold instruction on your transparent paper?
"""

assert(driver(test=True) == 17)
answer_a = driver()
write_solution('day13', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
Finish folding the transparent paper according to the instructions. 
The manual says the code is always eight capital letters.
What code do you use to activate the infrared thermal imaging camera system?
"""

answer_b = driver(one_fold=False)
write_solution('day13', 'b', answer_b)
# CURRENTLY: manual answer entry via inspecting output
# TODO: implement OCR to go from symbols to capital letter recognition?