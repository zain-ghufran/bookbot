
# ---------------------------
def count_words(text):
    words = text.split()
    return len(words)

# Creates a dictionary with a count of each character
def character_counter(text):
    # empty dictionary for storage
    letter_dic = {}
    # loops through each character in text
    for characters in text:
        # new variable that stores a .lowered version of each ccharacter
        converted_character = characters.lower()
        # if the lower case letter is not in the list, its value is set to one
        if converted_character not in letter_dic:
            # syntax is: empty_dict[key] = value
            letter_dic[converted_character] = 1
        # other wise, the count is added onto.
        else: 
            letter_dic[converted_character] += 1
    return letter_dic

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

# Converts dictionary to a list of sorted dictionaries
def dic_sort(letter_dic):
    # empty list for storage
    sorted_dics = []
    # This is how you utilize a loop to create another dictionary
    for char, count in letter_dic.items():
        # d creates a new dictionary from our looped variables
        d = {"char": char, "num": count}
        # append the list so that we have a list of dictionaries
        sorted_dics.append(d)
    sorted_dics.sort(reverse=True, key=sort_on)
    return sorted_dics








        
