def modify_string(text):
    if not isinstance(text, str):
        return "the input must be string"

    result = ""

    for ch in text:
        if ch.isupper():
            if result:              
                result += " "
            result += ch.lower()
        else:
            result += ch

    return result

print(modify_string("HelloWorld"))    
print(modify_string("AbdulmjeedBojeir"))        
