from aocd.models import Puzzle
from utils import get_specific_test_input, write_solution
from operator import mul, lt, gt, eq
from functools import reduce, partial

"""
Day 16: Packet Decoder
"""

puzzle = Puzzle(year=2021, day=16) 

def parse_A(packets): 
    
    def consume(n):
        nonlocal packets
        data, packets = packets[:n], packets[n:]
        return data
   
    version = int(consume(3), 2)
    T = int(consume(3), 2)
    if T == 4:
        while True:
            literal = consume(5)
            if literal[0] == '0':
                return version, packets
    I = int(consume(1), 2)
    if I == 0:
        L = int(consume(15), 2)
        subpackets = consume(L)
        while subpackets:
            ret_ver, subpackets = parse_A(subpackets)
            version += ret_ver
    elif I == 1:
        L = int(consume(11), 2)
        for _ in range(L):
            ret_ver, packets = parse_A(packets)
            version += ret_ver
    return version, packets

def parse_B(packets):
    
    def consume(n):
        nonlocal packets
        data, packets = packets[:n], packets[n:]
        return data

    version = int(consume(3), 2)
    type_id = int(consume(3), 2)
    if type_id == 4:
        value = ''
        while True:
            literal = consume(5)
            value += literal[1:]
            if literal[0] == '0':
                break
        value = int(value, 2)
        return value, packets
    length_type_id = int(consume(1), 2)
    values = []
    if length_type_id == 0:
        length = int(consume(15), 2)
        subpackets = consume(length)
        while subpackets:
            value, subpackets = parse_B(subpackets)
            values.append(value)
    elif length_type_id == 1:
        length = int(consume(11), 2)
        for _ in range(length):
            value, packets = parse_B(packets)
            values.append(value)
    return [
        sum, 
        partial(reduce, mul), 
        min, 
        max,
        None,
        lambda x: gt(*x),
        lambda x: lt(*x),
        lambda x: eq(*x)
    ][type_id](values), packets

def driver(part: str, test: bool=False, test_num: int=None):
    hex_packets = get_specific_test_input('day16', test_num).strip() if test else Puzzle(year=2021, day=16).input_data.strip()
    packets = ''.join([bin(int(c, 16))[2:].zfill(4) for c in hex_packets])
    parse_func = parse_A if part == 'A' else parse_B
    return parse_func(packets)[0]

assert driver(part='A', test=True, test_num=1) == 6
assert driver(part='A', test=True, test_num=2) == 16
assert driver(part='A', test=True, test_num=3) == 12
assert driver(part='A', test=True, test_num=4) == 23
assert driver(part='A', test=True, test_num=5) == 31
answer_a = driver(part='A')
write_solution('day16', 'a', answer_a)
# puzzle.answer_a = answer_a

assert driver(part='B', test=True, test_num=6) == 3
assert driver(part='B', test=True, test_num=7) == 54
assert driver(part='B', test=True, test_num=8) == 7
assert driver(part='B', test=True, test_num=9) == 9
assert driver(part='B', test=True, test_num=10) == 1
assert driver(part='B', test=True, test_num=11) == 0
assert driver(part='B', test=True, test_num=12) == 0
assert driver(part='B', test=True, test_num=13) == 1
answer_b = driver(part='B')
write_solution('day16', 'b', answer_b)
# puzzle.answer_b = answer_b