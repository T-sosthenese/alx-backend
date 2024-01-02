#!/usr/bin/env python3
"""
A module that implements FIFO caching system.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and is a caching system
    that implements FIFO caching algorithm.
    """
    def __init__(self):
        """
        Initializing the class
        """
        super().__init__()
        self.key_order = []  # Stores the order in which keys are inserted.

    def put(self, key, item):
        """
        A method that adds a key-value pair to the cache_data dictionary
        of the parent class
        """
        if key and item:
            self.cache_data[key] = item
            self.key_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

    def get(self, key):
        """
        A method that returns a value associated with a specific key in
        cache_data dictionary.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
