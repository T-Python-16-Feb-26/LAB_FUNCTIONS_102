def camel_to_sentence(text: str) -> str:
    """
    Convert a CamelCase string into a sentence with spaces and lowercase letters.

    Args:
        text (str): Input string in CamelCase format.

    Returns:
        str: Modified string with spaces before capital letters and all letters in lowercase.
    """

    result = "" 

    for char in text:

# Convert uppercase letters to lowercase and insert a space before them
        if char.isupper(): 
            result += " " + char.lower()

# Keep small letters, numbers, and symbols unchanged
        else:   
            result += char
            
    return result # Store the full sentence after formatting

user_input = input("Enter a sentence where each word starts with a capital letter (e.g., HelloWorld): ")
formatted_text = camel_to_sentence(user_input)
print("\nFormatted string:")
print(formatted_text)