
def separate_words(word:str):
    if type(word)==str:
        result = ""
        for char in word:
            if char.isupper():
                result += " " + char.lower()
            else:
                result += char
        return result.strip()
    else:
        return "not string"
    

print(separate_words("helloWorldThere "))