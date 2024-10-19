def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    frequency = {}

     # Count the frequency of each number
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the number with the highest frequency
    most_common = None
    max_count = 0
    for num, count in frequency.items():
        if count > max_count:
            most_common = num
            max_count = count
    
    return most_common