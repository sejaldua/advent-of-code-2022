from aocd.models import Puzzle
from utils import get_test_input, write_solution
import re
from collections import namedtuple

"""
Day 17: Trick Shot
"""

puzzle = Puzzle(year=2021, day=17) 

Velocity = namedtuple('Velocity', ['x', 'y'])
Position = namedtuple('Position', ['x', 'y'])
Target = namedtuple('Target', ['xmin', 'xmax', 'ymin', 'ymax'])

def parse_input(data: str) -> Target:
    pattern = r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)'
    return Target(*map(int, re.match(pattern, data).groups()))

"""
Part A:
- The probe's x position increases by its x velocity.
- The probe's y position increases by its y velocity.
- Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, 
  it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
- Due to gravity, the probe's y velocity decreases by 1.
Find the initial velocity that causes the probe to reach the highest y position 
and still eventually be within the target area after any step. What is the 
highest y position it reaches on this trajectory?
"""

def sum_n(n: int) -> int:
    return n * (n + 1) // 2

def part_a(test: bool=False) -> int:
    data = get_test_input('day17') if test else Puzzle(year=2021, day=17).input_data
    target = parse_input(data)
    
    # Minimum y position to reach trajectory and not overshoot
    return sum_n(target.ymin)

assert(part_a(test=True) == 45)
answer_a = part_a()
write_solution('day17', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B:
How many distinct initial velocity values cause the probe to be within the target area after any step?
"""

def simulate(init_velocity: Velocity, target: Target) -> bool:
    velocity = init_velocity
    pos = Position(x=0, y=0)
    while pos.x <= target.xmax and pos.y >= target.ymin:
        if pos.x >= target.xmin and pos.y <= target.ymax:
            return True
        pos = Position(
            x=pos.x + velocity.x,
            y=pos.y + velocity.y)
        velocity = Velocity(
            x=velocity.x - 1 if velocity.x > 0 else 0,
            y=velocity.y - 1)

def part_b(test: bool=False) -> int:
    data = get_test_input('day17') if test else Puzzle(year=2021, day=17).input_data
    target = parse_input(data)

    # Minimum x velocity to reach target is sqrt(2xmin)
    v_xmin = int((2 * target.xmin) ** 0.5)

    valid_velocities = 0
    for vx in range(v_xmin, target.xmax + 1):
        for vy in range(target.ymin, -target.ymin):
            if simulate(Velocity(vx, vy), target):
                valid_velocities += 1

    return valid_velocities

assert(part_b(test=True) == 112)
answer_b = part_b()
write_solution('day17', 'b', answer_b)
# puzzle.answer_b = answer_b