def separate_capitals(text):
    """
    This function checks if the parameter is a string.
    Then it separates words at capital letters,
    converts them to lowercase,
    and returns the modified string.
    """

    if not isinstance(text, str):
        return "Error: Parameter must be a string"

    result = ""

    for char in text:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char

    return result.strip()