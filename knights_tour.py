from typing import List, Tuple
from collections import deque

def knights_tour(n: int, start_x: int, start_y: int) -> List[Tuple[int, int]]:
    input_constraints = [
        n > 8,
        n < 5,
        start_x < 0,
        start_x >= n,
        start_y < 0,
        start_y >= n
    ]
    
    if any(input_constraints):
        raise ValueError("Your input does not match the accepted values")

