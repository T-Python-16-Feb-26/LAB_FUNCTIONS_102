def separates_word (word:str):
    if not word.isalpha():
        return "Please enter letters only" 

    result = ""

    for char in word:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char

    return result.strip()     

input_user=input("Type what you want: ")
print(separates_word(input_user))