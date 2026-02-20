#lab bonus function 102

def separates(string:str):
    '''This function will separate the words in a string by adding a space before each uppercase letter and converting it to lowercase.'''
    if not isinstance(string, str):
        return "Input must be a string"
    result = ""

    for char in string:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char
    return result
print(separates("helloWorldThere"))