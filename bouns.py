

def split_at_capitals(text):
    if type(text) != str:
        return "error: parameter must be a string"
    result = ""
    for i, ch in enumerate(text):
        if 'A' <= ch <= 'Z' and i != 0:
            result += " " + chr(ord(ch)+32)
        else:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch)+32)
            else:
                result +=ch
    return result

userinput = input("Please Enter Text You Want Split it: ")
print (split_at_capitals(userinput))
