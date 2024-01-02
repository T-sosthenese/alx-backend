#!/usr/bin/env python3
"""
A module that implements the LIFO caching algorithm.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class LIFOCache that inherits from BaseCaching.
    """
    def __init__(self):
        """
        Initializing the class instance.
        """
        super().__init__()
        self.key_order = []  # Stores keys that are discarded

    def put(self, key, item):
        """
        A method that adds a key-value pair to the cache_data dictionary
        of the parent class.
        """
        if key and item:
            self.cache_data[key] = item
            self.key_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(-2)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        A method that returns the value associated with a key in cache_data
        dictionary of the parent class.
        """
        if key in self.cache_data[key]:
            return self.cache_data[key]
        return None
