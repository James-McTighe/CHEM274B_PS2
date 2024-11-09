import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        # TODO: Implement
        pass
    
    def starts_with(self, prefix):
        # TODO: Implement
        pass

class BoggleBoard:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
    
    def generate_board(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return [[random.choice(alphabet) for _ in range(self.size)] for _ in range(self.size)]
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))

class BoggleSolver:
    def __init__(self, dictionary):
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word.upper())
    
    def find_words(self, board):
        found_words = set()
        for i in range(len(board)):
            for j in range(len(board)):
                self.dfs(board, i, j, "", set(), found_words)
        return list(found_words)
    
    def dfs(self, board:BoggleBoard, i:int, j:int, current_word:TrieNode, visited:set, found_words:set):
        exclusion_criteria = [
            i < 0,
            j < 0,
            i == board.size,
            j == board.size,
            (i,j) in visited,
            board[i][j] not in current_word.children,
        ]

        if any(exclusion_criteria):
            return
        
        visited.add((i,j))
        current_word = current_word.children[board[i][j]]


