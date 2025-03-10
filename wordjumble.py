import random 


#Hash Table (Dictionary)
word_dict = [
    "often",
    "kiosk",
    "immune",
    "cousin"
]

# letter postiions for larger word

secret_word = random.choice(word_dict)

jumbled = list(secret_word)
    
secret_word = random.choice(word_dict)
jumbled = list(secret_word)
random.shuffle(jumbled)

print("Jumbled Word List: ", jumbled)