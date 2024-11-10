from typing import List, Tuple

def knights_tour(n: int, start_x: int, start_y: int) -> List[Tuple[int, int]]:
    # Determines if a move is valid
    def is_valid(board, x, y):
        return 0 <= x < n and 0 <= y < n and board[y][x] == -1

    # Directions a knight can move (8 possibilities)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board = [[-1 for x in range(n)] for x in range(n)]
    
    board[start_y][start_x] = 0
    results = [(start_x, start_y)]

    def solver_utility(curr_x, curr_y, pos):
        if pos == n ** 2:
            return True

        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]

            # If the new position is valid and not visited
            if is_valid(board, new_x, new_y):
                board[new_y][new_x] = pos
                results.append((new_x, new_y))
                if solver_utility(new_x, new_y, pos + 1):
                    return True
                
                board[new_y][new_x] = -1
                results.pop()

        return False

    if solver_utility(start_x, start_y, 1):
        return results
    else:
        return []