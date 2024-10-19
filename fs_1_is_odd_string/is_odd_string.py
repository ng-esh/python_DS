def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
      # Initialize sum
    total = 0

    # Iterate over each character in the word
    for char in word:
        # Calculate character position ('a' = 1, 'b' = 2, ..., 'z' = 26)
        # ord('a') is 97, so we subtract 96 to get 'a' = 1
        total += ord(char.lower()) - 96

    # Return whether the total is odd
    return total % 2 == 1

    # Hint: you may find the ord() function useful here