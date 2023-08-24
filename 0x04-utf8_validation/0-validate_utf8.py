#!/usr/bin/python3
"""UTF8 validation."""


def validUTF8(data):
    """Helper function to check if the current byte
    is a valid continuation byte."""
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    """Helper function to get the number of
    bytes for the current UTF-8 character."""
    def get_num_bytes(byte):
        if (byte & 0b10000000) == 0b00000000:
            return 1
        elif (byte & 0b11100000) == 0b11000000:
            return 2
        elif (byte & 0b11110000) == 0b11100000:
            return 3
        elif (byte & 0b11111000) == 0b11110000:
            return 4
        else:
            return -1

    """Iterate through the data bytes."""
    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])
        if num_bytes == -1:
            return False

        """Check if the subsequent
        bytes are valid continuation bytes."""
        for j in range(i + 1, i + num_bytes):
            if j >= len(data) or not is_continuation(data[j]):
                return False

        i += num_bytes

    return True
