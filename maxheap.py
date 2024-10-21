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
        self._heapify_up(len(self.heap) - 1)

    def size(self):
        return len(self.heap)

    def _is_leaf(self, i):
        first_leaf = (self.size()//2) + 1
        last_leaf = self.size()
        leaf_indx = list(range(first_leaf,last_leaf))
        if i in leaf_indx:
            return True
        else:
            return False

    def _heapify_up(self, i):
        if i == 0:
            return 0
        parent = self.parent(i)
        if self.heap[parent] < self.heap[i]:
            self.swap(i,parent)
            self._heapify_up(parent)
        else:
            return self.heap[i]

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_down(self, i):

        # if self._is_leaf(i):
        #     return 0

        l_child = self.left_child(i)
        r_child = self.right_child(i)

        if l_child > self.size() or r_child > self.size():
            return None

        if l_child == None or r_child == None:
            return 0

        if self.heap[l_child] > self.heap[i]:
            self.swap(i,l_child)
            self._heapify_down(l_child)

        elif self.heap[r_child] > self.heap[i]:
            self.swap(i,r_child)
            self._heapify_down(r_child)

        else:
            return self.heap[i]
        

def heap_sort_descending(arr):
    heap = MaxHeap()
    # TODO
    pass

class LimitedMaxHeap(MaxHeap):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def insert(self, key):
        # TODO
        pass

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