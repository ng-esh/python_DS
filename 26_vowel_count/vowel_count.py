def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"  # String containing all the vowels
    freq_map = {}  # Dictionary to store the frequency of each vowel
    
    # Convert phrase to lowercase to make it case-insensitive
    phrase = phrase.lower()
    
    # Loop through each character in the phrase
    for char in phrase:
        if char in vowels:  # Check if the character is a vowel
            if char in freq_map:
                freq_map[char] += 1  # Increment the count of the vowel
            else:
                freq_map[char] = 1  # Initialize the count for the vowel
    
    return freq_map