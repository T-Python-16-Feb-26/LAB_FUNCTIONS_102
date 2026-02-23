def new_string(old_string):
    '''
    this checks if the string is a string,
    then takes capital letters and adds a space before them and makes them small

    args:
        old_string (str): the string to change

    returns:
        finished_string (str): the string after the changes

    '''
    finished_string = " "
    if type(old_string) != str:
        finished_string = "This is not a string"
        return finished_string
    
    for char in old_string:
        if char.isupper():
            char = char.lower()
            if finished_string[-1] == " ":
                finished_string += char
            else:
                finished_string += " " + char
        else:
            finished_string += char
    finished_string = finished_string[1:]
    return finished_string

print(new_string("HelloWorld There"))
    
