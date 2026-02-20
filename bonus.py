"""
# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```
"""

def no_to_capitalism(line):
    """
    This function takes a parameter checks if its a string (if not return it unchanged)
    the changes every capital letter with a small and space before it 
    """
    if isinstance(line, str):
        new_line = "" # create a string for the changes
        for i in line: # itrate through the string 
            if i.isupper(): # if capital is found change it to small and space before it
                new_line += " " + i.lower() 
            else: # else add the same 
                new_line += i

        return new_line.strip() # removes leading space if capital is in the begining 
    else:
        return line
    
print(no_to_capitalism("helloWorldThere")) # hello world there
print(no_to_capitalism("HelloWorldThere")) # hello world there
print(no_to_capitalism("HelloWorld1here")) # hello world1here
print(no_to_capitalism("1234")) # 1234
print(no_to_capitalism(True)) # True
print(no_to_capitalism(1234)) # 1234