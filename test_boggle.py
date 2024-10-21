import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from boggle import Trie, BoggleBoard, BoggleSolver

class TestBoggle(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        words = ["APPLE", "APP", "APPLY", "BAT", "BALL"]
        for word in words:
            self.trie.insert(word)

        dictionary = ["CAT", "CATS", "TACT", "STACK", "ACT", "ACTS"]
        self.solver = BoggleSolver(dictionary)

    # @weight(1)
    # @number("4.1")
    def test_search(self):
        self.assertTrue(self.trie.search("APPLE"))
        self.assertTrue(self.trie.search("APP"))
        self.assertFalse(self.trie.search("AP"))
        self.assertFalse(self.trie.search("APPL"))

    # @weight(1)
    # @number("4.2")    
    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("APP"))
        self.assertTrue(self.trie.starts_with("BA"))
        self.assertFalse(self.trie.starts_with("CAT"))

    # @weight(0)
    # @number("4.3")
    def test_board_size(self):
        board = BoggleBoard()
        self.assertEqual(len(board.board), 4)
        self.assertEqual(len(board.board[0]), 4)

    # @weight(0)
    # @number("4.4")    
    def test_custom_size(self):
        board = BoggleBoard(5)
        self.assertEqual(len(board.board), 5)
        self.assertEqual(len(board.board[0]), 5)

    # @weight(0)
    # @number("4.5")    
    def test_valid_characters(self):
        board = BoggleBoard()
        for row in board.board:
            for char in row:
                self.assertTrue(char.isalpha() and char.isupper())

    # @weight(1)
    # @number("4.6")
    def test_find_words(self):
        board = [
            ['C', 'A', 'T', 'S'],
            ['R', 'S', 'C', 'T'],
            ['L', 'O', 'A', 'K'],
            ['N', 'E', 'T', 'A']
        ]
        found_words = self.solver.find_words(board)
        expected_words = {"CAT", "CATS", "TACT", "STACK", "ACT", "ACTS"}
        self.assertEqual(set(found_words), expected_words)

    # @weight(1)
    # @number("4.7")    
    def test_no_words(self):
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X']
        ]
        found_words = self.solver.find_words(board)
        self.assertEqual(found_words, [])

    # @weight(1)
    # @number("4.8")    
    def test_all_words(self):
        board = [
            ['C', 'A', 'T', 'S'],
            ['T', 'A', 'C', 'T'],
            ['A', 'C', 'T', 'S'],
            ['S', 'T', 'A', 'K']
        ]
        found_words = self.solver.find_words(board)
        expected_words = {"CAT", "CATS", "TACT", "ACT", "ACTS"}
        self.assertEqual(set(found_words), expected_words)