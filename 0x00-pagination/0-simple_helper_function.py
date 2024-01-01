#!/usr/bin/env python3
"""
A module for calculating the start and end index of pagination
"""


def index_range(page, page_size):
    """
    Calculates the start and end index for a slice of a list
    parameters:
    page(int): The current page number
    page_size(int): The number of items per page
    Returns: A tuple containing the start and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
