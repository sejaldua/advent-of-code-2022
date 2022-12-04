from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 9: Smoke Basin
"""

puzzle = Puzzle(year=2021, day=9)

def parse_input(data):
    return np.array([list(map(int, list(line))) for line in data.splitlines()])

def compare_vals(val, adj_val):
    return True if val < adj_val else False
    
def coords_in_bounds(coords, bounds):
    return coords[0] in range(bounds[0]) and coords[1] in range(bounds[1])

def is_min_adjacent(heightmap, row, col):
     neighbors = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
     comparison_bools = []
     for adj_coords in neighbors:
         if coords_in_bounds(adj_coords, heightmap.shape):
             comparison_bools.append(compare_vals(heightmap[row][col], heightmap[adj_coords[0]][adj_coords[1]]))
     return all(comparison_bools)

def find_low_points(heightmap):
    low_points = []
    for row in range(heightmap.shape[0]):
        for col in range(heightmap.shape[1]):
            if is_min_adjacent(heightmap, row, col):
                low_points.append((row, col))
    return low_points

"""
Part A: 
- Each number corresponds to the height of a particular location, where 9 
  is the highest and 0 is the lowest a location can be.
- Your first goal is to find the low points - the locations that are lower than 
  any of its adjacent locations. Most locations have four adjacent locations 
  (up, down, left, and right); locations on the edge or corner of the map have 
  three or two adjacent locations, respectively. (Diagonal locations do not 
  count as adjacent.)
- The risk level of a low point is 1 plus its height. 
- Find all of the low points on your heightmap. What is the sum of the 
  risk levels of all low points on your heightmap?
"""

def part_a(test: bool = False) -> int:
    data = get_test_input('day09') if test else Puzzle(year=2021, day=9).input_data
    heightmap = parse_input(data)
    lp_coords = find_low_points(heightmap)
    lp_heights = list(map(lambda lp: heightmap[lp[0]][lp[1]], lp_coords))
    risk_levels = list(map(lambda x: x + 1, lp_heights))
    return sum(risk_levels)

assert(part_a(test=True) == 15)
answer_a = part_a()
write_solution('day09', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
- A basin is all locations that eventually flow downward to a single low 
  point. Therefore, every low point has a basin, although some basins are 
  very small. Locations of height 9 do not count as being in any basin, 
  and all other locations will always be part of exactly one basin.
- The size of a basin is the number of locations within the basin, 
  including the low point.
- What do you get if you multiply together the sizes of the three 
  largest basins?
"""

def breadth_first_search(heightmap, visited, init_coords):
    y, x = init_coords
    queue = [(y, x)]
    visited.add((y, x))
    count = 0
    while queue:
        y, x = queue.pop()
        count += 1
        for dy, dx in (0, -1), (0, 1), (-1, 0), (1, 0):
            if not coords_in_bounds((y + dy, x + dx), heightmap.shape) \
            or heightmap[y + dy][x + dx] == 9 \
            or heightmap[y + dy][x + dx] <= heightmap[y][x]:
                continue
            if (y + dy, x + dx) not in visited:
                queue.append((y + dy, x + dx))
                visited.add((y + dy, x + dx))
    return count, visited

def part_b(test: bool = False) -> int:
    data = get_test_input('day09') if test else Puzzle(year=2021, day=9).input_data
    heightmap = parse_input(data)
    lp_coords = find_low_points(heightmap)
    visited = set()
    basin_sizes = []
    for y, x in lp_coords:
        if (y, x) not in visited:
            basin_size, visited = breadth_first_search(heightmap, visited, (y, x))
            basin_sizes.append(basin_size)
    three_largest = sorted(basin_sizes, reverse=True)[:3]
    return np.prod(np.array(three_largest))
    
assert(part_b(test=True) == 1134)
answer_b = part_b()
write_solution('day09', 'b', answer_b)
# puzzle.answer_b = answer_b