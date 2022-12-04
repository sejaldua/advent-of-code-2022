from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 15: Chiton
"""

puzzle = Puzzle(year=2021, day=15) 

def init_total_costs(cost: np.ndarray) -> np.ndarray:
    """Minimum Cost Path, dynamic programming"""
    
    len_i, len_j = cost.shape
    total = np.zeros_like(cost)
    for i in range(1, len_i):
        total[i][0] = total[i - 1][0] + cost[i][0]
    for j in range(1, len_j):
        total[0][j] = total[0][j - 1] + cost[0][j]
    for i in range(1, len_i):
        for j in range(1, len_j):
            total[i][j] = min(total[i - 1][j], total[i][j - 1]) + cost[i][j]
    return total

def iterate_total_costs(cost: np.ndarray, total: np.ndarray) \
    -> tuple([np.ndarray, np.ndarray]):
    """Iterate on minimum cost path to allow backwards moves."""
    
    original_total = total.copy()
    R, C = cost.shape
    for i in range(0, R):
        for j in range(0, C):
            for adj_i, adj_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if adj_i < 0 or adj_i >= R:
                    continue
                if adj_j < 0 or adj_j >= C:
                    continue
                total[i, j] = min(total[i, j], total[adj_i, adj_j] + cost[i, j])
    if (total != original_total).any():
        return iterate_total_costs(cost, total)
    return cost, total

def expand_matrix(cost: np.ndarray, mult_factor: int=5) -> np.ndarray:
    """Expand matrix and wrap values to 1 if at 9"""
    
    def increment_cost(cost: np.ndarray) -> np.ndarray:
        new_costs = cost + 1
        new_costs[new_costs > 9] = 1
        return new_costs
    arrays = [cost]
    for _ in range(mult_factor - 1):
        arrays.append(increment_cost(arrays[-1]))
    slabs = [np.concatenate(arrays, axis=0)]
    for _ in range(mult_factor - 1):
        slabs.append(increment_cost(slabs[-1]))
    return np.concatenate(slabs, axis=1)

def get_lowest_risk_path(test: bool=False, expand: bool=False):
    """Driver function to get the lowest cost path through the matrix"""
    
    data = get_test_input('day15') if test else Puzzle(year=2021, day=15).input_data
    cost = np.array(list(map(lambda x: list(map(int, x)), data.splitlines())))
    if expand:
        cost = expand_matrix(cost)
    total = init_total_costs(cost)
    cost, total = iterate_total_costs(cost, total)
    return total[-1][-1]

"""
Part A:
You start in the top left position, your destination is the bottom right 
position, and you cannot move diagonally. The number at each position is 
its risk level; to determine the total risk of an entire path, add up the risk 
levels of each position you enter (that is, don't count the risk level of your 
starting position unless you enter it; leaving it adds no risk to your total).
Your goal is to find a path with the lowest total risk.
"""

assert(get_lowest_risk_path(test=True) == 40)
answer_a = get_lowest_risk_path()
write_solution('day15', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
The entire cave is actually five times larger in both dimensions than you 
thought; the area you originally scanned is just one tile in a 5x5 tile area 
that forms the full map. Your original map tile repeats to the right and 
downward; each time the tile repeats to the right or downward, all of its risk 
levels are 1 higher than the tile immediately up or left of it. However, risk 
levels above 9 wrap back around to 1.
Using the full map, what is the lowest total risk of any path from the top 
left to the bottom right?
"""

assert(get_lowest_risk_path(test=True, expand=True) == 315)
answer_b = get_lowest_risk_path(expand=True)
write_solution('day15', 'b', answer_b)
# puzzle.answer_b = answer_b