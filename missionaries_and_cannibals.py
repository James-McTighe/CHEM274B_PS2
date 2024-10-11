from collections import deque

class State:
    def __init__(self, m_left, c_left, boat, m_right, c_right, parent=None, move=None):
        self.m_left = m_left
        self.c_left = c_left
        self.boat = boat
        self.m_right = m_right
        self.c_right = c_right
        self.parent = parent
        self.move = move

    def is_valid(self):
        if self.m_left >= 0 and self.c_left >= 0 and self.m_right >= 0 and self.c_right >= 0 \
           and (self.m_left == 0 or self.m_left >= self.c_left) \
           and (self.m_right == 0 or self.m_right >= self.c_right):
            return True
        return False

    def is_goal(self):
        return self.m_left == 0 and self.c_left == 0

    def __eq__(self, other):
        return self.m_left == other.m_left and self.c_left == other.c_left \
               and self.boat == other.boat and self.m_right == other.m_right \
               and self.c_right == other.c_right

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.boat, self.m_right, self.c_right))

def get_successors(state):
    successors = []
    if state.boat == 'left':
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = State(state.m_left - m, state.c_left - c, 'right',
                              state.m_right + m, state.c_right + c, state, (m, c, 'right'))
            if new_state.is_valid():
                successors.append(new_state)
    else:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = State(state.m_left + m, state.c_left + c, 'left',
                              state.m_right - m, state.c_right - c, state, (m, c, 'left'))
            if new_state.is_valid():
                successors.append(new_state)
    return successors

def solve_missionaries_cannibals():
    initial_state = State(3, 3, 'left', 0, 0)
    if initial_state.is_goal():
        return [initial_state]

    frontier = deque([initial_state])
    explored = set()

    while frontier:
        state = frontier.popleft()
        if state.is_goal():
            path = []
            while state:
                path.append(state)
                state = state.parent
            return path[::-1]

        explored.add(state)

        for successor in get_successors(state):
            if successor not in explored and successor not in frontier:
                frontier.append(successor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found!")
    else:
        print("Solution found!")
        for i, state in enumerate(solution):
            if i == 0:
                print("Initial state:")
            else:
                print(f"\nMove {i}:")
                print(f"  {state.move[0]} missionaries and {state.move[1]} cannibals " 
                      f"move to the {state.move[2]} bank.")
            print(f"  Left bank: {state.m_left}M {state.c_left}C")
            print(f"  Right bank: {state.m_right}M {state.c_right}C")
        print("\nGoal state reached!")

if __name__ == "__main__":
    solution = solve_missionaries_cannibals()
    print_solution(solution)