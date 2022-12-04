from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 3: Binary Diagnostic
"""

puzzle = Puzzle(year=2021, day=3)

def get_mode(bits):
    return str(int(sum(bits) >= len(list(filter(lambda x: x == 0, bits)))))

def get_anti_mode(bits):
    return str(int(sum(bits) < len(list(filter(lambda x: x == 0, bits)))))

def get_transposed(data):
    int_array = list(map(lambda line: [int(char) for char in list(line)], data))
    return [list(i) for i in zip(*int_array)]

"""
Part A: 
Each bit in the gamma rate can be determined by finding the MOST common bit in 
the corresponding position of all numbers in the diagnostic report.
Each bit in the epsilon rate can be determined by finding the LEAST common bit.
Use the binary numbers in your diagnostic report to calculate the gamma rate 
and epsilon rate, then multiply them together. What is the power consumption of 
the submarine?
"""

def part_a(test=False):
    data = get_test_input('day03').splitlines() if test else Puzzle(year=2021, day=3).input_data.splitlines()
    transposed = get_transposed(data)
    gamma_bits = list(map(lambda bits: get_mode(bits), transposed))
    epsilon_bits = list(map(lambda x: '0' if x == '1' else '1', gamma_bits))
    gamma_rate = int("".join(gamma_bits), 2)
    epsilon_rate = int("".join(epsilon_bits), 2)  
    return gamma_rate * epsilon_rate

assert(part_a(test=True) == 198)
answer_a = part_a()
write_solution('day03', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B:
Verify the life support rating, which can be determined by multiplying the 
oxygen generator rating by the CO2 scrubber rating.
Before searching for either rating value, start with the full list of binary 
numbers from your diagnostic report and consider just the first bit of those 
numbers. Then:
    - Keep only numbers selected by the bit criteria for the type of rating 
    value for which you are searching. Discard numbers which do not match the 
    bit criteria.
    - If you only have one number left, stop; this is the rating value for 
    which you are searching.
    - Otherwise, repeat the process, considering the next bit to the right.
    
The bit criteria depends on which type of rating value you want to find:
    - To find oxygen generator rating, determine the MOST common value (0 or 1) 
    in the current bit position, and keep only numbers with that bit in that 
    position. If 0 and 1 are equally common, keep values with a 1 in the 
    position being considered.
    - To find CO2 scrubber rating, determine the least common value (0 or 1) in 
    the current bit position, and keep only numbers with that bit in that 
    position. If 0 and 1 are equally common, keep values with a 0 in the 
    position being considered.
"""

def get_rating(data, anti=False):
    filtered = data.copy()
    fxn = get_anti_mode if anti else get_mode
    bit_pos = 0
    while len(filtered) > 1:
        transposed = get_transposed(filtered)
        filtered = [num for num in filtered if num[bit_pos] == fxn(transposed[bit_pos])]
        bit_pos += 1
    return int("".join(filtered[0]), base=2)

def part_b(test=False):
    data = get_test_input('day03').splitlines() if test else Puzzle(year=2021, day=3).input_data.splitlines()
    oxygen_generator_rating = get_rating(data, anti=False)
    co2_scrubber_rating = get_rating(data, anti=True)
    return oxygen_generator_rating * co2_scrubber_rating

assert(part_b(test=True) == 230)
answer_b = part_b()
write_solution('day03', 'b', answer_b)
# puzzle.answer_b = answer_b