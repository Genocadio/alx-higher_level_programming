def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string  # Return the original string if index is out of range

    result = ""
    for i in range(len(string)):
        if i != n:
            result += string[i]

    return result
