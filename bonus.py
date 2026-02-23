

def bonus_function(word):
    if type(word) != str:
        return ("type must be a string!")
    
    result_tring = " " 
    for character in word:
        if character.isupper():
            result_tring = result_tring + " " + character.lower()
        else:
            result_tring =result_tring + character     
    return result_tring

print(bonus_function("HiEveryOne"))                

