'''write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !'''

def words (text: str):
    '''this function to takes a string as a parameter'''
    if not isinstance (text,str):
        return "Error , input must be string  "
    result = text[0].lower()
    for char in text[1:] :
        if char.isupper():
            result += " " + char.lower()
        else : 
            result += char
    return result 

print(words("HelloWorld"))
print(words(True))