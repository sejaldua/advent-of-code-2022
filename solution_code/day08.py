from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 8: Seven Segment Search
"""

puzzle = Puzzle(year=2021, day=8)

SEGMENT_MAPPING = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
}

def parse_input(data):
    for line in data.splitlines():
        signals, outputs = line.strip().split(" | ")
        yield signals.split(), outputs.split()

"""
Part A: 
Because the digits 1, 4, 7, and 8 each use a unique number of segments, 
you should be able to tell which combinations of signals correspond to those
digits. In the output values, how many times do digits 1, 4, 7, or 8 appear?
"""

def decode_fixed_len(output):
    """
        {'c', 'f'}                              -->     1
        {'b', 'c', 'd', 'f'}                    -->     4
        {'a', 'c', 'f'}                         -->     7
        {'a', 'b', 'c', 'd', 'e', 'f', 'g'}     -->     8
    """
    letters_to_len = dict(cf=1, bcdf=4, acf=7, abcdefg=8)
    fixed_len_to_digit = {len(k): v for k, v in letters_to_len.items()}
    return 1 if len(output) in fixed_len_to_digit else 0
    
def part_a(test: bool = False) -> int:
    data = get_test_input('day08') if test else Puzzle(year=2021, day=8).input_data
    return sum([sum([decode_fixed_len(output) for output in outputs]) for _, outputs in parse_input(data)])

assert(part_a(test=True) == 26)
answer_a = part_a()
write_solution('day08', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
Mapping logic puzzle:
-> 1, 4, 7, 8 are always unique.
-> Segment a is determined by set difference between 7 and 1.
-> 2, 3, 5 signals are of length 5.
-> 0, 6, 9 signals are of length 6.
-> In 2, 3, 5 combined, a, d, and g will be counted thrice. (adg)
-> Segment bd is determined from set diff of four and one.
-> Segment dg is determined from adg - a.
-> Segment be is determined from bcef - df (1).
-> Segments d, b, e, g, can then be derived.
-> We can determine 6 now by checking where d and e is both present
    in length 6 items.
-> Using six we can get c and f.
Finally we do a translation between encoded digits and numbers based on
this information.
We can use the SEGMENT_MAPPING to map the sequence of digits into numbers.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
"""

def decode_number(digit, mapping):
    translate = lambda imap: ''.join(sorted([mapping[i] for i in imap]))
    new_mapping = {translate(v): k for k, v in SEGMENT_MAPPING.items()}
    digit_sorted = ''.join(sorted(digit))
    return new_mapping[digit_sorted]

def get_mapping(signals: list) -> dict:
    # Take unique numbers.
    one   = list(filter(lambda x: len(x) == 2, signals))[0]
    four  = list(filter(lambda x: len(x) == 4, signals))[0]
    seven = list(filter(lambda x: len(x) == 3, signals))[0]
    eight = list(filter(lambda x: len(x) == 7, signals))[0]

    l_fives = list(filter(lambda x: len(x) == 5, signals)) # Two, Five, or Three
    l_six = list(filter(lambda x: len(x) == 6, signals)) # Six, Nine or Zero
    l_fives_s = ''.join(l_fives)

    seg_a = set(seven) - set(one)

    seg_bd = set.symmetric_difference(set(four), set(one))
    seg_dg = set([x for x in l_fives_s if l_fives_s.count(x) == 3]) - seg_a
    seg_be = set([x for x in l_fives_s if l_fives_s.count(x) != 3]) - set(one)
    
    seg_d = set.intersection(seg_dg, seg_bd)
    seg_b = set.intersection(seg_be, seg_bd)

    a = list(seg_a)[0]
    e = list(seg_be - seg_b)[0]
    g = list(seg_dg - seg_d)[0]
    b = list(seg_b)[0]
    d = list(seg_d)[0]

    six = [x for x in l_six if d in x and e in x][0]

    seg_c = set(eight) - set(six)
    seg_f = set(one) - seg_c

    c = list(seg_c)[0]
    f = list(seg_f)[0]

    mapping = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g}
    return mapping

def part_b(test: bool = False, data=None):
    if not data:
        data = get_test_input('day08') if test else Puzzle(year=2021, day=8).input_data
    output_sums = 0
    for signals, outputs in parse_input(data):
        mapping = get_mapping(signals)
        decoded = [decode_number(output, mapping) for output in outputs]
        output_sums += int(''.join(map(str, decoded)))
    return output_sums

assert(part_b(test=True, data="acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf") == 5353)
assert(part_b(test=True) == 61229)
answer_b = part_b()
write_solution('day08', 'b', answer_b)
# puzzle.answer_b = answer_b
