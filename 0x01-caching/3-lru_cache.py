#!/usr/bin/env python3
"""
Module that implements least recently used (LRU) algorithm
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class LRU cache inheriting from BaseCaching
    """
    def __init__(self):
        """
        Initializing the class
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.cache_data_list.pop(0)
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))

    def get(self, key):
        """
        Retrieves an item from the cache based on the key
        """
        if key:
            if key in self.cache_data:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
