#!/usr/bin/env python3
"""
Implementation of MRU caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inheriting from BaseCaching class.
    """
    def __init__(self):
        """
        Initializing the class
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        Adding a key-value pair to the cache_data dictionary.
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.cache_data_list.pop(-2)
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key:
            if key in self.cache_data:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
