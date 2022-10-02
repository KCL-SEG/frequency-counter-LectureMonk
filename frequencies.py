"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        # Presence Check
        if (not frequencies.get(str(item))):
            # Not Found - add item
            frequencies[str(item)] = 1
        else:
            # Found - increment freq
            frequencies[str(item)] = frequencies.get(str(item)) + 1
    return frequencies
