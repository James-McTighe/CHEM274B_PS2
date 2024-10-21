import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from maxheap import MaxHeap, LimitedMaxHeap, heap_sort_descending

class TestValidSymbols(unittest.TestCase):
    # @weight(1)
    # @number("2.1")
    def test_insert_and_extract(self):
        heap = MaxHeap()
        heap.insert(4)
        heap.insert(2)
        heap.insert(9)
        heap.insert(7)
        heap.insert(5)
        self.assertEqual(heap.extract_max(), 9)
        self.assertEqual(heap.extract_max(), 7)
        self.assertEqual(heap.extract_max(), 5)
        self.assertEqual(heap.extract_max(), 4)
        self.assertEqual(heap.extract_max(), 2)
        self.assertIsNone(heap.extract_max())
    
    # @weight(1)
    # @number("2.2")
    def test_empty_heap(self):
        heap = MaxHeap()
        self.assertIsNone(heap.extract_max())
    
    # @weight(1)
    # @number("2.3")
    def test_single_element(self):
        heap = MaxHeap()
        heap.insert(42)
        self.assertEqual(heap.extract_max(), 42)
        self.assertIsNone(heap.extract_max())

    # @weight(1)
    # @number("2.4")
    def test_heap_sort_descending(self):
        arr = [4, 10, 3, 5, 1]
        sorted_arr = heap_sort_descending(arr)
        self.assertEqual(sorted_arr, [10, 5, 4, 3, 1])

    # @weight(1)
    # @number("2.5")
    def test_heap_sort_empty(self):
        arr = []
        sorted_arr = heap_sort_descending(arr)
        self.assertEqual(sorted_arr, [])

    # @weight(1)
    # @number("2.6")
    def test_heap_sort_single_element(self):
        arr = [42]
        sorted_arr = heap_sort_descending(arr)
        self.assertEqual(sorted_arr, [42])

    # @weight(1)
    # @number("2.7")
    def test_heap_sort_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = heap_sort_descending(arr)
        self.assertEqual(sorted_arr, [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1])

    # @weight(1)
    # @number("2.8")
    def test_limited_heap(self):
        heap = LimitedMaxHeap(3)
        heap.insert(4)
        heap.insert(2)
        heap.insert(9)
        heap.insert(7)
        heap.insert(5)
        self.assertEqual(len(heap.heap), 3)
        self.assertEqual(heap.extract_max(), 5)
        self.assertEqual(heap.extract_max(), 4)
        self.assertEqual(heap.extract_max(), 2)
        self.assertIsNone(heap.extract_max())

    # @weight(1)
    # @number("2.9")
    def test_limited_heap_all_smaller(self):
        heap = LimitedMaxHeap(3)
        heap.insert(9)
        heap.insert(7)
        heap.insert(5)
        heap.insert(4)
        heap.insert(2)
        self.assertEqual(len(heap.heap), 3)
        self.assertEqual(heap.extract_max(), 5)
        self.assertEqual(heap.extract_max(), 4)
        self.assertEqual(heap.extract_max(), 2)
        self.assertIsNone(heap.extract_max())

    # @weight(1)
    # @number("2.10")
    def test_limited_heap_mixed(self):
        heap = LimitedMaxHeap(3)
        heap.insert(6)
        heap.insert(1)
        heap.insert(9)
        heap.insert(11)
        heap.insert(5)
        self.assertEqual(len(heap.heap), 3)
        self.assertEqual(heap.extract_max(), 6)
        self.assertEqual(heap.extract_max(), 5)
        self.assertEqual(heap.extract_max(), 1)
        self.assertIsNone(heap.extract_max())