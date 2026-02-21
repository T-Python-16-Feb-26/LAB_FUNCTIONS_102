def small_letters(sentence:str)->str:
    if not isinstance(sentence, str):
        return "Input must be a string."
    
    result = ""
    for char in sentence:
        if char.isupper():
            result+=" "+char.lower()
        else:
            result+=char
    return result.strip()
    
print(small_letters("helloWorldThere"))
print(small_letters(123))
