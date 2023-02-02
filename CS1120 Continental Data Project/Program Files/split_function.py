def split_function(string: str, separator: str) -> list[str]:
    """Takes a string and a separator and splits the string on the separator.
     Returns a list of separated string segments.
     """

    separator_size = len(separator)
    if separator_size == 0:
        raise ValueError("Empty separator.")

    starting_index = 0
    ending_index = len(string) - separator_size
    result = []

    while starting_index <= ending_index:
        segment = string[starting_index: starting_index + separator_size]
        if segment != separator:
            starting_index += 1
            continue
        result.append(string[:starting_index])
        string = string[starting_index + separator_size:]
        starting_index = 0
        ending_index = len(string) - separator_size
    result.append(string)

    return result
