def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
# Iterate through the list, checking every 3 consecutive numbers
    for i in range(len(nums) - 2):
        # Calculate the sum of the three consecutive numbers
        if sum(nums[i:i+3]) % 2 != 0:
            return True
    
    # Return False if no such set of three numbers is found
    return False