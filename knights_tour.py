from typing import List, Tuple
from collections import deque


def knights_tour(n: int, start_x: int, start_y: int) -> List[Tuple[int, int]]:
    # Determines the validity of a particular move
    def is_safe(board,x,y):
        input_constraints = [
        n < 8,
        n > 5,
        x > 0,
        x <= n,
        y > 0,
        y <= n,
        board[y][x] == -1
    ]
        if all(input_constraints):
            return True
        else:
            return False
    
    board = [[-1 for x in range(n)]for y in range(n)]
    # Each index is a valid move combination for a knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[start_x][start_y] = 0
    pos = 1
    results = []

    def solveKTUtil(curr_x, curr_y):
        nonlocal pos
        if pos == n ** 2:
            return
        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]
            if is_safe(board,new_x, new_y):
                pos += 1
                board[new_x][new_y] = pos
                results.append((new_x,new_y))
                solveKTUtil(new_x,new_y)

    solveKTUtil(start_x,start_y)
    return results

