import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from knights_tour import knights_tour

class TestKnightsTour(unittest.TestCase):
    def validate_tour(self, n, tour):
        if tour is None:
            return False
        if len(tour) != n * n:
            return False
        visited = set()
        for i in range(len(tour) - 1):
            x1, y1 = tour[i]
            x2, y2 = tour[i + 1]
            if (x1, y1) in visited or not (0 <= x1 < n and 0 <= y1 < n):
                return False
            visited.add((x1, y1))
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            if (dx, dy) not in [(1, 2), (2, 1)]:
                return False
        x, y = tour[-1]
        return (x, y) not in visited and (0 <= x < n and 0 <= y < n)

    @weight(1)
    @number("21.1")
    def test_5x5_board(self):
        result = knights_tour(5, 0, 0)
        self.assertEqual(len(result), 25)
        self.assertEqual(len(set(result)), 25)

    @weight(1)
    @number("21.2")
    def test_6x6_board(self):
        result = knights_tour(6, 2, 2)
        self.assertEqual(len(result), 36)
        self.assertEqual(len(set(result)), 36)

    @weight(1)
    @number("21.3")
    def test_7x7_board(self):
        result = knights_tour(7, 3, 3)
        self.assertEqual(len(result), 49)
        self.assertEqual(len(set(result)), 49)

    @weight(1)
    @number("21.4")
    def test_8x8_board(self):
        result = knights_tour(8, 0, 0)
        self.assertEqual(len(result), 64)
        self.assertEqual(len(set(result)), 64)

    @weight(1)
    @number("21.5")
    def test_start_corner(self):
        result = knights_tour(5, 0, 0)
        self.assertEqual(result[0], (0, 0))

    @weight(1)
    @number("21.6")
    def test_start_center(self):
        result = knights_tour(5, 2, 2)
        self.assertEqual(result[0], (2, 2))
    
    @weight(1)
    @number("21.7")
    def test_all_squares_visited(self):
        result = knights_tour(6, 0, 0)
        visited = set(result)
        all_squares = {(x, y) for x in range(6) for y in range(6)}
        self.assertEqual(visited, all_squares)

    @weight(1)
    @number("21.8")
    def test_valid_knight_moves(self):
        result = knights_tour(5, 0, 0)
        for i in range(1, len(result)):
            x1, y1 = result[i-1]
            x2, y2 = result[i]
            dx, dy = abs(x2 - x1), abs(y2 - y1)
            self.assertTrue((dx == 2 and dy == 1) or (dx == 1 and dy == 2))
