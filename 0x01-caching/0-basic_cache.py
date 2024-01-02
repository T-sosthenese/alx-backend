#!/usr/bin/env python3
"""
A caching system class implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache: A class that inherits from BasicCaching and serves as
    a caching system.
    """
    def __init__(self):
        """
        A class constructor
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        A class method that is used to assign an item to a key and stores
        the value in the cache_data class variable of the parent class.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        A method that returns a value that is associated to a specific
        key in the data_cache dictionary.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
