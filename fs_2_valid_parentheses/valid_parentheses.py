def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
     # Initialize counter for open parentheses
    balance = 0
    
    # Iterate through each character in the string
    for char in parens:
        if char == '(':
            balance += 1  # Increment for an opening parenthesis
        elif char == ')':
            balance -= 1  # Decrement for a closing parenthesis
        
        # If balance becomes negative, there are unmatched closing parentheses
        if balance < 0:
            return False

    # If balance is zero, parentheses are balanced
    return balance == 0