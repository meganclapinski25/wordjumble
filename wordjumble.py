import random 


#Hash Table (Dictionary)
word_dict = [
    "often",
    "kiosk",
    "immune",
    "cousin"
]

# letter postiions for larger word

# secret_word = random.choice(word_dict)

# jumbled = list(secret_word)
    
# secret_word = random.choice(word_dict)
# jumbled = list(secret_word)
# random.shuffle(jumbled)

# jumbled = ''.join(jumbled)

# print("Jumbled Word List: ", jumbled)

def jumble_word(word_list):
    jumbled_words = []
    for word in word_list:
        jumbled = list(word)
        random.shuffle(jumbled)
        jumbled_words.append(''.join(jumbled))
    return jumbled_words


jumbled_words = jumble_word(word_dict)

jumbled_words = jumble_word(word_dict)
print("Jumbled Words:", jumbled_words)       