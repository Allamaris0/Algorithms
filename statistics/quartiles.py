def quartile(array: list, quart: 1 or 2 or 3):
    """The function uses the method with excluding a median when length of an array is odd"""
    array = sorted(array)
    length = len(array)
    half = length // 2

    def median(some_array):
        l = len(some_array)
        h = l // 2
        if l % 2 == 0:
            return (some_array[h - 1] + some_array[h]) / 2
        else:
            return some_array[h]

    if quart == 1:
        return median(array[0:half])
    elif quart == 2:
        return median(array)
    elif quart == 3:
        if length % 2 == 0:
            return median(array[half:length])
        else:
            return median(array[half + 1:length])