from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution
import re

"""
Day 5: Supply Stacks
"""

puzzle = Puzzle(year=2022, day=5)

def parse_stacks(lines: list) -> list:
    """ Parse stacks from the input file """

    # number of stacks (last number of the line with the stacks numbers)
    num_stacks = int(re.findall('(\d+)', lines[-1])[-1])

    # create empty stacks
    stacks = [[] for _ in range(num_stacks)]

    # "[X] [Y] [Z]" -> ["X", "Y", "Z"]
    for line in lines[:-1][::-1]:
        for i in range(num_stacks):
            elem = line[(i*4)+1]
            if elem != ' ':
                stacks[i].append(elem)

    return stacks

def read_message(stacks: list) -> str:
    """ Get the final message """
    # get le last letter (=top) of each stack
    return ''.join([stack[-1] for stack in stacks])

"""
Part A: 
After the rearrangement procedure completes, what crate ends up on top of each stack?
"""

def CrateMover9000(stacks: list, moves: list) -> list:
    """ Apply the moves (of the form "move X from Y to Z") to the stacks
        (One crate at a time : CrateMover 9000)"""
    for move in moves:
        # parse numbers from a string of the form "move X from Y to Z"
        num_moves, start, end = [int(x) for x in re.findall('\d+', move)]

        # LIFO
        for _ in range(num_moves):
            crate = stacks[start-1].pop()
            stacks[end-1].append(crate)

    return stacks

def part_a(test=False):
    data = get_test_input('day05') if test else Puzzle(year=2022, day=5).input_data
    puzzle, instructions = data.split('\n\n')
    puzzle = puzzle.splitlines()
    instructions = instructions.splitlines()
    stacks = parse_stacks(puzzle)
    stacks = CrateMover9000(stacks, instructions)
    message = read_message(stacks)
    return message

assert(part_a(test=True) == 'CMZ')
answer_a = part_a()
write_solution('day05', 'a', answer_a)
puzzle.answer_a = answer_a  

"""
Part B:
Same problem as Part A, but FIFO instead of LIFO this time
"""

def CrateMover9001(stacks: list, moves: list) -> list:
    """ Apply the moves (of the form "move X from Y to Z") to the stacks
        (One crate at a time : CrateMover 9000)"""
    for move in moves:
        # parse numbers from a string of the form "move X from Y to Z"
        num_moves, start, end = [int(x) for x in re.findall('\d+', move)]

        # FIFO
        queue = []
        for _ in range(num_moves):
            queue.append(
                stacks[start-1].pop()
            )
        
        for crate in queue[::-1]:
            stacks[end-1].append(crate)

    return stacks

def part_b(test=False):
    data = get_test_input('day05') if test else Puzzle(year=2022, day=5).input_data
    puzzle, instructions = data.split('\n\n')
    puzzle = puzzle.splitlines()
    instructions = instructions.splitlines()
    stacks = parse_stacks(puzzle)
    stacks = CrateMover9001(stacks, instructions)
    message = read_message(stacks)
    return message

assert(part_b(test=True) == 'MCD')
answer_b = part_b()
write_solution('day05', 'b', answer_b)
puzzle.answer_b = answer_b