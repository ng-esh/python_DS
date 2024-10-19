def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    seen = set()  # A set to keep track of the numbers we've seen
    
    for num in nums:
        complement = goal - num  # The number that would make the pair sum to goal
        if complement in seen:
            return (complement, num)  # Return the pair that sums to goal
        seen.add(num)  # Add the current number to the set if it hasn't been seen before
    
    return ()  # Return empty tuple if no pair is found
