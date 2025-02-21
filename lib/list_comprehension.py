#!/usr/bin/env python3

def return_evens(numbers):
    """Returns a list of even numbers from the given list."""
    return [num for num in numbers if num % 2 == 0]

def make_exclamation(sentences):
    """Returns a list of sentences with an exclamation mark at the end."""
    return [sentence + "!" for sentence in sentences]
