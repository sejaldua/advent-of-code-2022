from aocd.models import Puzzle
from utils import get_test_input, write_solution
from collections import Counter

"""
Day 14: Extended Polymerization
"""

puzzle = Puzzle(year=2021, day=14)

def extract_data(data: str) -> tuple:
    """ Extract polymer template and pair insertion rules """
    
    polymer, rules = data.split('\n\n')
    rules = dict(list(map(lambda x: x.split(' -> '), rules.splitlines())))
    return polymer, rules    

"""
Part A:
- The first line is the polymer template - this is the starting point of 
  the process.
- The following section defines the pair insertion rules. A rule like AB -> C 
  means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.
  - Because all pairs are considered simultaneously, inserted elements are 
    not considered to be part of a pair until the next step.
- Apply 10 steps of pair insertion to the polymer template and find the 
  most and least common elements in the result. 
What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""

def perform_step(polymer: str, rules: dict) -> str:
    """
    Performs a single step of polymerization by performing all applicable insertions; returns new polymer template string
    """
    
    new = [polymer[i] + rules[polymer[i:i+2]] for i in range(len(polymer)-1)]
    new.append(polymer[-1])
    return "".join(new)
    
def part_a(iterations: int=10, test: bool=False, ) -> int:
    """ 
    Non-scalable polymerizer which performs actual pair insertions
    """
    
    data = get_test_input('day14') if test else Puzzle(year=2021, day=14).input_data
    polymer, rules = extract_data(data)
    for _ in range(iterations):
        polymer = perform_step(polymer, rules)
    return polymer.count(max(polymer, key = polymer.count)) - polymer.count(min(polymer, key = polymer.count))

assert(part_a(iterations=10, test=True) == 1588)
answer_a = part_a(iterations=10)
write_solution('day14', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
Now apply 40 steps of pair insertion to the polymer template...
What do you get if you take the quantity of the most common element 
and subtract the quantity of the least common element?
"""

def part_b(iterations: int=40, test: bool=False):
    """
    Scalable polymerizer which uses Counters rather than
    actually performing pair insertions
    """
    
    data = get_test_input('day14') if test else Puzzle(year=2021, day=14).input_data
    polymer, rules = extract_data(data)
    
    # initialize pair counter and letter counter
    pair_ctr = Counter(a + b for a, b in zip(polymer, polymer[1:]))
    letter_ctr = Counter(polymer)
    
    # perform desired number o steps, updatign the pair counter each time
    for _ in range(iterations):
        new_pair_ctr = Counter()
        for pair, count in pair_ctr.items():
            insert = rules[pair]
            for new_pair in (pair[0] + insert), (insert + pair[1]):
                new_pair_ctr[new_pair] += count
            letter_ctr[insert] += count
        pair_ctr = new_pair_ctr

    # num occurrences of most common minus num occurrences of least common
    return letter_ctr.most_common()[0][1] - letter_ctr.most_common()[-1][1]

assert(part_b(iterations=10, test=True) == 1588)
assert(part_b(iterations=40, test=True) == 2188189693529)
answer_b = part_b(iterations=40)
write_solution('day14', 'b', answer_b)
# puzzle.answer_b = answer_b