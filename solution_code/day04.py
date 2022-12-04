from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 4: Giant Squid
"""

puzzle = Puzzle(year=2021, day=4)

def parse_raw_data(data):
    draws, *boards = data.split('\n\n')
    draws = list(map(int, draws.split(',')))
    boards = [{
        'values': 
            [
                [int(cell) for cell in row.split(' ') if cell != '']
                for row in board.split('\n')
            ],
        'markers': 
            [
                [0 for i in range(5)] 
                for j in range(5)
            ]
        }
        for board in boards
    ]
    return draws, boards

def get_board_dicts(boards):
    board_dicts = [
            {
                cell: (x, y)
                for x, row in enumerate(board['values'])
                for y, cell in enumerate(row)
            }
            for board in boards
        ]
    return board_dicts

def check_markers(arr):
    t_arr = [list(i) for i in zip(*arr)]
    if any(list(map(lambda x: True if sum(x) == len(arr) else False, arr))):
        return True
    elif any(list(map(lambda x: True if sum(x) == len(arr) else False, t_arr))):
        return True
    else:
        return False
    
"""
Part A: 
Bingo with many boards... find the board that wins first and will defeat the
giant squid. To calculate the score of the winning board, start by finding 
the sum of all unmarked numbers on that board. Then, multiply that sum by the
number that was just called when the board won. To guarantee victory against 
the giant squid, figure out which board will win first. What will your final 
score be if you choose that board?
"""

def part_a(test=False):
    data = get_test_input('day04') if test else Puzzle(year=2021, day=4).input_data
    draws, boards = parse_raw_data(data)
    board_dicts = get_board_dicts(boards)
    for draw in draws:
        for i, board in enumerate(boards):
            try:
                row, col = board_dicts[i][draw]
                board['markers'][row][col] += 1
                if check_markers(board['markers']):
                    marked_vals = np.array(board['values']) * np.array(board['markers'])
                    unmarked_sum = np.sum(board['values']) - np.sum(marked_vals)
                    return unmarked_sum * draw
            except KeyError:
                continue
    
assert(part_a(test=True) == 4512)
answer_a = part_a()
write_solution('day04', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
Figure out which board will win last. Once it wins, what would its final 
score be?
"""

def part_b(test=False):
    data = get_test_input('day04') if test else Puzzle(year=2021, day=4).input_data
    draws, boards = parse_raw_data(data)
    board_dicts = get_board_dicts(boards)
    for draw in draws:
        board_states = [int(not check_markers(board['markers'])) for board in boards]
        num_no_bingo_yet = sum(board_states)
        for i, board in enumerate(boards):
            try:
                row, col = board_dicts[i][draw]
                board['markers'][row][col] += 1
                if check_markers(board['markers']) and num_no_bingo_yet == 1 and i == board_states.index(1):
                    marked_vals = np.array(board['values']) * np.array(board['markers'])
                    unmarked_sum = np.sum(board['values']) - np.sum(marked_vals)
                    return unmarked_sum * draw
            except KeyError:
                continue
    
assert(part_b(test=True) == 1924)
answer_b = part_b()
write_solution('day04', 'b', answer_b)
# puzzle.answer_b = answer_b