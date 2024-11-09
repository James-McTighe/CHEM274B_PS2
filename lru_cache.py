import time
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

class LRUCacheWithExpiration:
    def __init__(self, capacity: int, expiration_time: int):
        self.capacity = capacity
        self.expiration_time = expiration_time
        self.cache = OrderedDict()
        self.timestamps = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        if (time.time() - self.timestamps[key]) > self.expiration_time:
            self.cache.pop(key)
            return -1
        self.cache.move_to_end(key)
        self.timestamps.update({key:time.time()})
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        self.timestamps.update({key:time.time()})
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

class LRUCacheWithCallbacks:
    def __init__(self, capacity: int, on_eviction=None):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.on_eviction = on_eviction

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            evicted_item_key, evicted_item_value = self.cache.popitem(last=False)
            
            if self.on_eviction != None:
                self.on_eviction(evicted_item_key, evicted_item_value)