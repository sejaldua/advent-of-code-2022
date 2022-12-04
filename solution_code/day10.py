from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 10: Syntax Scoring
"""

puzzle = Puzzle(year=2021, day=10)

OPENING_CHARS = ['(', '[', '{', '<']
CLOSING_CHARS = [')', ']', '}', '>']
PAIRS = dict(zip(OPENING_CHARS, CLOSING_CHARS))

CORRUPTED_POINTS = [3, 57, 1197, 25137]
CORRUPTED_SCORING_TABLE = dict(zip(CLOSING_CHARS, CORRUPTED_POINTS))

INCOMPLETE_SCORING_TABLE = {k: i+1 for i, k in enumerate(CLOSING_CHARS)}

def check_syntax(line):
    stack = []
    for char in line:
        if char in OPENING_CHARS:
            stack.append(PAIRS[char])
        elif char in CLOSING_CHARS:
            if stack[-1] == char:
                stack.pop()
            # CORRUPTED
            else:
                # first illegal character
                return char
    # INCOMPLETE
    if stack:
        stack.reverse()
        # string of closing characters to complete the line
        return "".join(stack)

"""
Part A: 
Every chunk must open and close with one of four legal pairs of 
matching characters:
- If a chunk opens with (, it must close with ).
- If a chunk opens with [, it must close with ].
- If a chunk opens with {, it must close with }.
- If a chunk opens with <, it must close with >.
Some lines are incomplete, but others are corrupted. 
Find and discard the corrupted lines first.
A corrupted line is one where a chunk closes with the wrong character.
Stop at the first incorrect closing character on each corrupted line.
To calculate the syntax error score for a line, take the first illegal 
character on the line and look it up in the following table:
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.
Find the first illegal character in each corrupted line of the 
navigation subsystem. What is the total syntax error score for those errors?
"""

def part_a(test: bool = False) -> int:
    data = get_test_input('day10') if test else Puzzle(year=2021, day=10).input_data
    data = list(map(list, data.splitlines()))
    # only consider corrupted lines, discard all incomplete lines
    corrupted_chars = [check_syntax(line) for line in data if check_syntax(line) in CLOSING_CHARS]
    syntax_error_scores = list(map(lambda x: CORRUPTED_SCORING_TABLE[x], corrupted_chars))
    return sum(syntax_error_scores)
    

assert(part_a(test=True) == 26397)
answer_a = part_a()
write_solution('day10', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
Now, discard the corrupted lines. The remaining lines are incomplete.
Incomplete lines don't have any incorrect characters - instead, 
they're missing some closing characters at the end of the line. 
To repair the navigation subsystem, you just need to figure out the 
sequence of closing characters that complete all open chunks in the line.
You can only use closing characters (), ], }, or >), and you must add them 
in the correct order so that only legal pairs are formed and all chunks 
end up closed.
The score is determined by considering the completion string 
character-by-character. Start with a total score of 0. Then, for each 
character, multiply the total score by 5 and then increase the total score 
by the point value given for the character in the following table:
    ): 1 point.
    ]: 2 points.
    }: 3 points.
    >: 4 points.
Find the completion string for each incomplete line, score the completion 
strings, and sort the scores. What is the middle score?
"""

def compute_completion_str_score(completion_str):
    score = 0
    for char in completion_str:
        score = (score * 5) + INCOMPLETE_SCORING_TABLE[char]
    return score

def part_b(test: bool = False) -> int:
    data = get_test_input('day10') if test else Puzzle(year=2021, day=10).input_data
    data = list(map(list, data.splitlines()))
    # only consider incomplete lines, discard all corrupted lines
    completion_strs = [check_syntax(line) for line in data if check_syntax(line) not in CLOSING_CHARS]
    completion_str_scores = list(map(compute_completion_str_score, completion_strs))
    middle_score = sorted(completion_str_scores)[len(completion_str_scores) // 2]
    return middle_score
    
assert(part_b(test=True) == 288957)
answer_b = part_b()
write_solution('day10', 'b', answer_b)
# puzzle.answer_b = answer_b