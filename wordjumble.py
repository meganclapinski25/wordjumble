import random 

#Hash Table (Dictionary)
word_dict = {
    'tefon': "often",
    'sokik': "kiosk",
    'niumem': "immune",
    "siconu": "cousin"
}

# letter postiions for larger word
postions = {
    'often': [2,4],
    'kiosk':[0,1,3],
    "immune":[4],
    "cousin":[3,4]
}

#Game Function 
def play_game():
    
    for jumbled_word in word_dict.keys():
        correct_word = word_dict[jumbled_word]
        print(f"Unscrambled this word:{jumbled_word}")