from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 2: Rock Paper Scissors
"""

puzzle = Puzzle(year=2022, day=2)

"""
Part A: 
Rock paper scissors scoring
total score = shape you selected + outcome of the round
    - shape you selected:
        Rock (A, X) => 1
        Paper (B, Y) => 2
        Scissors (C, Z)=> 3
    - outcomes of the round:
        Loss => 0
        Draw => 3
        Win => 6
"""

def score(p1, p2):
    '''they are p1, you are p2'''
    your_shape = p2 + 1
    their_shape = p1 + 1
    outcome_mapping = {'win': 6, 'draw': 3, 'loss': 0}
    if (their_shape - 2) % 3 == your_shape - 1:
        outcome = 'loss'
    elif (your_shape - 2) % 3 == their_shape - 1:
        outcome = 'win'
    else:
        outcome = 'draw'
    return your_shape + outcome_mapping[outcome]

def part_a(test=False):
    data = get_test_input('day02') if test else Puzzle(year=2022, day=2).input_data
    data = data.splitlines()
    data = [line.split() for line in data]
    # map letters to numbers using 'A' and 'X' as anchors
    data = [(ord(p1) - ord("A"), ord(p2) - ord("X")) for p1, p2 in data]
    return sum(score(p1, p2) for p1, p2 in data)

assert(part_a(test=True) == 15)
answer_a = part_a()
write_solution('day02', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
The second letter now represents the desired outcome:
    X => loss
    Y => draw
    Z => win
"""

def part_b(test=False):
    data = get_test_input('day02') if test else Puzzle(year=2022, day=2).input_data
    data = data.splitlines()
    data = [line.split() for line in data]
    # map letters to numbers using 'A' and 'X' as anchors
    data = [(ord(p1) - ord("A"), ord(p2) - ord("X")) for p1, p2 in data]
    return sum(score(p1, (p1 + p2 - 1) % 3) for p1, p2 in data)

assert(part_b(test=True) == 12)
answer_b = part_b()
write_solution('day02', 'b', answer_b)
puzzle.answer_b = answer_b