#!/usr/bin/python3

"""Module for UTF-8 validation"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list of int): A list of integers where each integer represents 1 byte
                        of data. Only the 8 least significant bits of each
                        integer are considered.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits of the integer
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                # Single byte characters must start with 0xxxxxxx
                return False
        else:
            # Continuation bytes must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    # Ensure there are no remaining expected continuation bytes
    return n_bytes == 0
