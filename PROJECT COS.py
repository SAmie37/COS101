import json

# Initial dictionary data
indian_dict = {
    "Namaste": "A traditional Indian greeting, often meaning 'I bow to the divine in you'.",
    "Atithi": "A Sanskrit word meaning 'guest', based on the belief that 'the guest is God'.",
    "Satyagraha": "A philosophy of non-violent resistance, famously associated with Mahatma Gandhi.",
    "Guru": "A spiritual teacher or mentor, especially in Indian religions like Hinduism, Buddhism, and Sikhism.",
    "Dharma": "A key concept in Indian religions, referring to duty, law, righteousness, or moral order.",
    "Karma": "The belief that one's actions (good or bad) determine future consequences, central to Hinduism, Buddhism, and Jainism.",
    "Yoga": "A spiritual, mental, and physical practice originating from India, aimed at achieving spiritual union and self-realization.",
    "Swaraj": "Self-rule or self-governance, famously advocated by Mahatma Gandhi in the Indian independence movement.",
    "Mahatma": "A title meaning 'great soul', most famously used for Mahatma Gandhi, a leader of India's independence movement.",
    "Pukka": "A word of Hindi origin meaning authentic, genuine, or of high quality. Used in British English as well.",
    "Bindi": "A decorative mark worn on the forehead, often associated with Hindu culture, representing the 'third eye'.",
    "Veda": "Ancient sacred texts of India, considered the foundation of Hindu religious knowledge and wisdom.",
    "Mandala": "A geometric figure representing the universe, used in Hinduism and Buddhism as a symbol of meditation and cosmic unity.",
    "Raga": "A traditional melodic framework in Indian classical music, each raga is associated with specific emotions and times of day.",
    "Sari": "A traditional Indian garment worn by women, usually consisting of a long piece of cloth draped elegantly around the body.",
    "Diwali": "A major Hindu festival known as the 'Festival of Lights', celebrating the victory of good over evil and light over darkness.",
    "Durga": "A Hindu goddess associated with strength, protection, and motherhood, often depicted riding a lion or tiger.",
    "Ayurveda": "An ancient system of natural healing and medicine that originated in India, focusing on balance in the body, mind, and spirit.",
    "Chai": "A popular Indian beverage made with tea, milk, sugar, and spices like cardamom, cinnamon, and ginger."
}

# Function to search the dictionary (case-insensitive)
def search_word(word):
    word = word.capitalize()  # Capitalize to match the dictionary keys
    if word in indian_dict:
        return indian_dict[word]
    else:
        return "Sorry, the word is not found in the dictionary."

# Function to add a new word to the dictionary
def add_word(word, meaning):
    word = word.capitalize()  # Ensure the word is capitalized for consistency
    if word in indian_dict:
        return f"The word '{word}' already exists in the dictionary."
    else:
        indian_dict[word] = meaning
        return f"Word '{word}' added successfully."

# Function to edit an existing word's meaning
def edit_word(word, new_meaning):
    word = word.capitalize()
    if word in indian_dict:
        indian_dict[word] = new_meaning
        return f"Meaning of '{word}' updated successfully."
    else:
        return f"Sorry, the word '{word}' does not exist in the dictionary."

# Function to delete a word from the dictionary
def delete_word(word):
    word = word.capitalize()
    if word in indian_dict:
        del indian_dict[word]
        return f"Word '{word}' deleted successfully."
    else:
        return f"Sorry, the word '{word}' does not exist in the dictionary."

# Function to list all words in the dictionary
def list_words():
    return "\n".join(sorted(indian_dict.keys()))

# Function to save the dictionary to a JSON file
def save_to_file(filename="indian_dict.json"):
    with open(filename, "w") as file:
        json.dump(indian_dict, file, indent=4)
    return f"Dictionary saved to {filename}."
# Function to load the dictionary from a JSON file
def load_from_file(filename="indian_dict.json"):
    global indian_dict
    try:
        with open(filename, "r") as file:
            indian_dict = json.load(file)
        return "Dictionary loaded from file successfully."
    except FileNotFoundError:
        return "No saved dictionary found, starting with the default one."

# Main interaction loop
def main():
    print("Welcome to the Indian Dictionary!")
    while True:
        print("\nSelect an option:")
        print("1. Search a word")
        print("2. Add a new word")
        print("3. Edit an existing word")
        print("4. Delete a word")
        print("5. List all words")
        print("6. Save dictionary to file")
        print("7. Load dictionary from file")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            word = input("Enter a word to search: ").strip()
            print(search_word(word))

        elif choice == "2":
            word = input("Enter the word to add: ").strip()
            meaning = input("Enter the meaning: ").strip()
            print(add_word(word, meaning))

        elif choice == "3":
            word = input("Enter the word to edit: ").strip()
            new_meaning = input("Enter the new meaning: ").strip()
            print(edit_word(word, new_meaning))

        elif choice == "4":
            word = input("Enter the word to delete: ").strip()
            print(delete_word(word))

        elif choice == "5":
            print("List of all words in the dictionary:")
            print(list_words())

        elif choice == "6":
            print(save_to_file())

        elif choice == "7":
            print(load_from_file())

        elif choice == "8":
            print("Thank you for using the Indian Dictionary. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the dictionary program
if  'name' == "main":
    main()