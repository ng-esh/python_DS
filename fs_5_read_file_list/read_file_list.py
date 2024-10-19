def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Strip the newline character and print with the "- " prefix
                print(f"- {line.strip()}")
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!