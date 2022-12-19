from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution
import re

"""
Day 6: Tuning Trouble
"""

puzzle = Puzzle(year=2022, day=6)

def solution(num_chars, test=False, data=None):
    data = data if test else Puzzle(year=2022, day=6).input_data
    for i, char in enumerate(data):
        if len(set(data[i:i+num_chars])) == num_chars:
            return i+num_chars
    return -1

"""
Part A: 
How many characters need to be processed before the first start-of-packet marker is detected?
NOTE: a packet requires 4 unique characters
"""

assert(solution(4, test=True, data='mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7)
assert(solution(4, test=True, data='bvwbjplbgvbhsrlpgdmjqwftvncz') == 5)
assert(solution(4, test=True, data='nppdvjthqldpwncqszvftbrmjlhg') == 6)
assert(solution(4, test=True, data='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10)
assert(solution(4, test=True, data='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11)
answer_a = solution(4)
write_solution('day06', 'a', answer_a)
puzzle.answer_a = answer_a  

"""
Part B:
How many characters need to be processed before the first start-of-message marker is detected?
NOTE: a message requires 14 unique characters
"""

assert(solution(14, test=True, data='mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19)
assert(solution(14, test=True, data='bvwbjplbgvbhsrlpgdmjqwftvncz') == 23)
assert(solution(14, test=True, data='nppdvjthqldpwncqszvftbrmjlhg') == 23)
assert(solution(14, test=True, data='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29)
assert(solution(14, test=True, data='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26)
answer_b = solution(14)
write_solution('day06', 'b', answer_b)
puzzle.answer_b = answer_b