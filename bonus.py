def string_function(string_parameter: str) -> str:
    
    if not isinstance(string_parameter, str):
        return "Input must be a string."
    
    modified_string = ""

    for char in string_parameter:
        if char.isupper():
            modified_string += " " + char.lower()
        else:
            modified_string += char
    
    return modified_string

print(string_function("helloWorldThere"))