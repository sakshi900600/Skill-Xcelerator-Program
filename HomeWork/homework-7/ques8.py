# 8. Implement LRU (Least Recently Used) Cache 
# Description: Design a data structure for an LRU cache using deque (or doubly linked list + hashmap). 
# Input: 
# cache = LRUCache(2) 
# cache.put(1, 1) 
# cache.put(2, 2) 
# print(cache.get(1))  # returns 1 
# cache.put(3, 3)      # evicts key 2 
# print(cache.get(2))  # returns -1 (not found) 


class LRUCache():
    def __init__(self):
        pass