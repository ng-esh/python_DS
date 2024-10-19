def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    # Step 1: Find all the vowels in the string and store them in reverse order
    vowel_list = [char for char in s if char in vowels]
    vowel_list.reverse()

    # Step 2: Rebuild the string with vowels replaced by reversed ones
    result = []
    vowel_index = 0
    for char in s:
        if char in vowels:
            result.append(vowel_list[vowel_index])
            vowel_index += 1
        else:
            result.append(char)
    
    # Return the final string with vowels reversed
    return ''.join(result)