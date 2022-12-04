from aocd.models import Puzzle
from utils import get_specific_test_input, write_solution

"""
Day 12: Passage Pathing
"""

puzzle = Puzzle(year=2021, day=12)

def assemble_adjacency_list(lines: list) -> dict:
    """ Assemble the adjacency list from rough map / cave connectivity input"""
    
    src_dest_pairs = [tuple(line.split('-')) for line in lines]
    nodes = list(set([node for tup in src_dest_pairs for node in tup]))
    graph = dict().fromkeys(nodes, [])
    for src, dest in src_dest_pairs:
        if dest not in graph[src] and dest != 'start':
            graph[src] = [*graph[src], dest]
        if src not in graph[dest] and src != 'start':
            graph[dest] = [*graph[dest], src]
    return graph       

def depth_first_traversal(graph, currentVertex, visited, flag: bool=False) -> list:
    """Depth first traversal to find all paths from 'start' to 'end'

    Args:
        graph (list): adjacency list
        currentVertex (str): string (key into adjacency list)
        visited (list): current traversal path
        flag (bool, optional): whether or not a lowercase node can be visited 
        twice; defaults to False; flips from True to False if applicable

    Returns:
        list: Unique paths from 'start' to 'end' fulfilling the specified cave 
        path traversal criteria
    """
    
    visited.append(currentVertex)
    if currentVertex == 'end':
        return [visited]
    paths = []
    for vertex in graph[currentVertex]:
        if vertex not in visited or vertex.isupper():
            new_paths = depth_first_traversal(graph, vertex, visited.copy(), flag)
            paths.extend(new_paths)
        elif vertex.islower() and flag:
            new_paths = depth_first_traversal(graph, vertex, visited.copy(), not flag)
            paths.extend(new_paths)
    return paths

def driver(test: bool=False, test_num: int=None, flag: bool=False) -> int:
    """ Driver which works for Part A and B, only arg to flip is flag"""
    
    data = get_specific_test_input('day12', test_num).splitlines() if test else Puzzle(year=2021, day=12).input_data.splitlines()
    graph = assemble_adjacency_list(data)
    paths = depth_first_traversal(graph, 'start', [], flag)
    return len(paths)

"""
Part A:
Your goal is to find the number of distinct paths that start at start, 
end at end, and don't visit small caves more than once. There are two types of 
caves: big caves (written in uppercase, like A, which can be visited any 
number of times) and small caves (written in lowercase, like b).
How many paths through this cave system are there that visit small caves at most once?
"""

assert(driver(test=True, test_num=1) == 10)
assert(driver(test=True, test_num=2) == 19)
assert(driver(test=True, test_num=3) == 226)
answer_a = driver()
write_solution('day12', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
Now big caves can be visited any number of times, a single small cave can 
be visited at most twice, and the remaining small caves can be visited at 
most once.
The caves named start and end can only be visited exactly once each: once 
you leave the start cave, you may not return to it, and once you reach the 
end cave, the path must end immediately.
Given these new rules, how many paths through this cave system are there?
"""

assert(driver(test=True, test_num=1, flag=True) == 36)
assert(driver(test=True, test_num=2, flag=True) == 103)
assert(driver(test=True, test_num=3, flag=True) == 3509)
answer_b = driver(flag=True)
write_solution('day12', 'b', answer_b)
# puzzle.answer_b = answer_b