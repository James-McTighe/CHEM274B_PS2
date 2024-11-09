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

    def search(self, word) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.is_end_of_word == True:
            return True

    def starts_with(self, prefix) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class BoggleBoard:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()

    def generate_board(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return [
            [random.choice(alphabet) for _ in range(self.size)]
            for _ in range(self.size)
        ]

    def print_board(self):
        for row in self.board:
            print(" ".join(row))


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

    def dfs(
        self,
        board: list,
        i: int,
        j: int,
        current_word: str,
        visited: set,
        found_words: set,
    ) -> set:
        exclusion_criteria = [
            i < 0,
            j < 0,
            i == len(board),
            j == len(board),
            (i, j) in visited,
        ]
        # Base Case to return if the word doesn't match our criteria
        if any(exclusion_criteria):
            return

        visited.add((i, j))
        # node =
        current_word += board[i][j]

        if self.trie.search(current_word):
            found_words.add(current_word)

        if self.trie.starts_with(current_word):
            self.dfs(board, i + 1, j, current_word, visited, found_words)
            self.dfs(board, i - 1, j, current_word, visited, found_words)
            self.dfs(board, i, j + 1, current_word, visited, found_words)
            self.dfs(board, i, j - 1, current_word, visited, found_words)
            self.dfs(board, i + 1, j + 1, current_word, visited, found_words)
            self.dfs(board, i - 1, j - 1, current_word, visited, found_words)
            self.dfs(board, i - 1 , j + 1, current_word, visited, found_words)
            self.dfs(board, i + 1, j - 1, current_word, visited, found_words)
        
        visited.remove((i,j))

        return found_words
