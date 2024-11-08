class MaxHeap:
    def __init__(self):
        self.heap = []

    
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(self.size - 1)

    @property
    def size(self):
        return len(self.heap)

    def _is_leaf(self, i):
        if i >= self.size // 2:
            return True
        else:
            return False

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def _heapify_down(self, i):
        largest = i
        l = self.left_child(i)
        r = self.right_child(i)
        
        if l < self.size and self.heap[l] > self.heap[largest]:
            largest = l

        if r < self.size and self.heap[r] > self.heap[largest]:
            largest = r
        
        if largest != i:
            self.swap(i,largest)
            self._heapify_down(largest)
        
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

        

def heap_sort_descending(arr):
    heap = MaxHeap()
    for i in arr:
        heap.insert(i)

    sorted_arr = []

    while heap.size > 0:
        sorted_arr.append(heap.extract_max())
        
    return sorted_arr

class LimitedMaxHeap(MaxHeap):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def insert(self, key):
        
        if self.size < self.max_size:
            self.heap.append(key)
            self._heapify_up(len(self.heap) - 1)

# *********************************
#            Testing
# *********************************


a = MaxHeap()

for i in range(10):
    a.insert(i)

print(a.heap)
a.heap[0] = -1
print(a.heap)
a._heapify_down(0)
print(a.heap)
print(a.extract_max())