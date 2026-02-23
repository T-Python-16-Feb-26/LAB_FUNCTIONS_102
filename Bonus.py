def split_camel_case(text):
    if not isinstance(text, str):
        return "Error: Input must be a string"

    result = ""
    for char in text:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char
    return result.strip()
print(split_camel_case("helloWorldThere"))
