def string_check (text):
    if not isinstance(text, str):
        return "the input must be a string"

    modified_String = ""

    for char in text:
        if char.isupper():
            modified_String += " " + char.lower()
        else:
            modified_String += char

    return modified_String

input_text = input("please enter a string text: ")
output_text = string_check(input_text)
print("the modified string is:", output_text)