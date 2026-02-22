def checkAndParseStr(usrStr:str):
    '''
    this function takes  a string and checks if the input is a string, 
    then it seperates the word from any uppercase letter 
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