import random 


#Hash Table (Dictionary)
word_dict = [
    "often",
    "kiosk",
    "immune",
    "cousin"
]

letter_postitions = [
    [3,5],
    [1,2,4],
    [5],
    [4,5]
]

# letter postiions for larger word

# secret_word = random.choice(word_dict)

# jumbled = list(secret_word)
    
# secret_word = random.choice(word_dict)
# jumbled = list(secret_word)
# random.shuffle(jumbled)

# jumbled = ''.join(jumbled)

# print("Jumbled Word List: ", jumbled)

def jumble_word(word_list, letter_list):
    jumbled_words = []
    final_letters = []
    
    # jumble all the words 
    for word, positions in word_list, letter_list:
        jumbled = list(word)
        random.shuffle(jumbled)
        jumbled_words.append(''.join(jumbled))
        
    # Extract the letters at the correct postions 
    
        extracted_letters = [word[pos-1] for pos in positions]
        final_letters.append(extracted_letters)
    
    return jumbled_words, final_letters

    


jumbled_words, final_letters = jumble_word(word_dict, letter_postitions)

# Print the jumbled words
print("Jumbled Words:")
for word in jumbled_words:
    print(word)

# Print the letters for the final puzzle
print("\nLetters for the final puzzle:")
for letters in final_letters:
    print("".join(letters))