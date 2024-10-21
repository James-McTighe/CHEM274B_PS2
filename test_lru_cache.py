import time, unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from lru_cache import LRUCache, LRUCacheWithExpiration, LRUCacheWithCallbacks

class TestLRUCache(unittest.TestCase):
    # @weight(0)
    # @number("17.1")
    def test_basic_operations(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    # @weight(0)
    # @number("17.2")
    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 2)

    # @weight(0)
    # @number("17.3")
    def test_time_complexity(self):
        cache = LRUCache(10000)
        start_time = time.time()
        for i in range(100000):
            cache.put(i, i)
        end_time = time.time()
        put_time = (end_time - start_time) / 100000
        
        start_time = time.time()
        for i in range(100000):
            cache.get(i)
        end_time = time.time()
        get_time = (end_time - start_time) / 100000
        
        self.assertLess(put_time, 0.0001)  # Expecting O(1) time complexity
        self.assertLess(get_time, 0.0001)  # Expecting O(1) time complexity

    # @weight(1)
    # @number("17.4")
    def test_expiration(self):
        cache = LRUCacheWithExpiration(2, 1)  # 1 second expiration
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)
        time.sleep(1.1)
        self.assertEqual(cache.get(1), -1)

    # @weight(1)
    # @number("17.5")
    def test_update_expiration_on_get(self):
        cache = LRUCacheWithExpiration(2, 2)  # 2 second expiration
        cache.put(1, 1)
        time.sleep(1)
        self.assertEqual(cache.get(1), 1)  # This should update the timestamp
        time.sleep(1.5)
        self.assertEqual(cache.get(1), 1)  # Should still be valid

    # @weight(1)
    # @number("17.6")
    def test_time_complexity(self):
        cache = LRUCacheWithExpiration(10000, 3600)  # 1 hour expiration
        start_time = time.time()
        for i in range(100000):
            cache.put(i, i)
        end_time = time.time()
        put_time = (end_time - start_time) / 100000
        
        start_time = time.time()
        for i in range(100000):
            cache.get(i)
        end_time = time.time()
        get_time = (end_time - start_time) / 100000
        
        self.assertLess(put_time, 0.0001)  # Expecting O(1) time complexity
        self.assertLess(get_time, 0.0001)  # Expecting O(1) time complexity

    # @weight(1)
    # @number("17.7")
    def test_eviction_callback(self):
        evicted_items = []
        def on_eviction(key, value):
            evicted_items.append((key, value))

        cache = LRUCacheWithCallbacks(2, on_eviction)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(evicted_items, [(1, 1)])
        cache.put(4, 4)
        self.assertEqual(evicted_items, [(1, 1), (2, 2)])

    # @weight(1)
    # @number("17.8")
    def test_update_existing_key_no_eviction(self):
        evicted_items = []
        def on_eviction(key, value):
            evicted_items.append((key, value))

        cache = LRUCacheWithCallbacks(2, on_eviction)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)
        self.assertEqual(evicted_items, [])
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 2)

    # @weight(1)
    # @number("17.9")
    def test_time_complexity(self):
        cache = LRUCacheWithCallbacks(10000)
        start_time = time.time()
        for i in range(100000):
            cache.put(i, i)
        end_time = time.time()
        put_time = (end_time - start_time) / 100000
        
        start_time = time.time()
        for i in range(100000):
            cache.get(i)
        end_time = time.time()
        get_time = (end_time - start_time) / 100000
        
        self.assertLess(put_time, 0.0001)  # Expecting O(1) time complexity
        self.assertLess(get_time, 0.0001)  # Expecting O(1) time complexity
  