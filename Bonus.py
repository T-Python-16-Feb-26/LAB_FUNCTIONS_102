def funcStr(text:str):
    if type(text) != str:
        return"error:input must be string"
    result= " "
    for char in text:
       if char.isupper():
           result += " "+ char.lower()
       else:
           result+=char
    return result
print(funcStr("HI SHARIFAH"))
         