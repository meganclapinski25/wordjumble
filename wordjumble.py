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

def word_jumble(word_list, letter_list):
    jumbled_words = []
    final_letters = []
    
    # jumble all the words 
    for i in range(len(word_list)):
        word = word_list[i]
        positions = letter_list[i]
        
        
        jumbled = list(word)
        random.shuffle(jumbled)
        jumbled_words.append(''.join(jumbled))
        
    # Extract the letters at the correct postions 
    
        extracted_letters = [word[pos-1] for pos in positions]
        final_letters.append(extracted_letters)
    
    return jumbled_words, final_letters

    
def jumble_game():
    jumbled_words, final_letters = word_jumble(word_dict, letter_postitions)
    
    correct_letters = []
    
    words_solved = 0
    
    while words_solved < len(jumbled_words):
        jumbled_word = jumbled_words[words_solved]
        correct_positions = final_letters[words_solved]
        
        print(f"Jumbled Word: {jumbled_word}")
        guess = input("Your guess:").strip()
        
        if guess == word_dict[i]:
            print("Correct you have solved the word")
            correct_letters.extend(correct_positions)
            words_solved +=1 
        else:
            print("That is not correct, try again")
            
        print("Game Over, you have solved all the jumbled words")
        print("Here is the final puzzle:")
        print("".join(correct_letters))

jumble_game()
# print("Jumbled Words:")
# for word in jumbled_words:
#     print(word)

# # Print the letters for the final puzzle
# print("\nLetters for the final puzzle:")
# for letters in final_letters:
#     print("".join(letters))