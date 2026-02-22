def checkAndParseStr(usrStr:str):
    '''
    - first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```

    '''
    if type(usrStr) != str:
        return "Error: Input is not a string"
    modified_str = ''
    for char in usrStr:
        if char.isupper():
            modified_str += ' ' + char.lower()
        else:
            modified_str += char
    return modified_str.strip()
user_input = input("Enter a string: ")
result = checkAndParseStr(user_input)
print(result)