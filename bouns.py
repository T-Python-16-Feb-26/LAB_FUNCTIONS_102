def format_string(text):

    if not type(text)==str:
        return "it should be str"

    result = ""
    

    for char in text:
        
        if char.isupper():
            
            result += " " + char.lower()
            
        else:
            result+=char
            
    return result


example = "helloWorldThere"
print(format_string(example))
