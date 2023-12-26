import json

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(dictionary, file_path):
    with open(file_path, 'w') as file:
        json.dump(dictionary, file, indent=2)

def search_word(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        return "Word not found in the dictionary."

def add_word(dictionary, word, definition, synonyms, examples):
    dictionary[word] = {
        'definition': definition,
        'synonyms': synonyms,
        'examples': examples
    }
    save_data(dictionary, 'data.json')
    print("Word added successfully!")

def update_definition(dictionary, word, new_definition):
    if word in dictionary:
        dictionary[word]['definition'] = new_definition
        save_data(dictionary, 'data.json')
        print("Definition updated successfully!")
    else:
        print("Word not found in the dictionary.")

def display_all_words(dictionary):
    if not dictionary:
        print("No words in the dictionary.")
    else:
        for word in dictionary:
            print(f"- {word}")

def main():
    file_path = '
    
    data.json'
    dictionary = load_data(file_path)

    while True:
        print("\nMenu:")
        print("1. Search for a word")
        print("2. Add a new word")
        print("3. Update definition of a word")
        print("4. Display all words")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            word_to_search = input("Enter a word to search: ")
            result = search_word(dictionary, word_to_search)
            print(result)

        elif choice == '2':
            new_word = input("Enter a new word: ")
            new_definition = input("Enter the definition: ")
            new_synonyms = input("Enter synonyms (comma-separated): ").split(', ')
            new_examples = input("Enter examples (comma-separated): ").split(', ')
            add_word(dictionary, new_word, new_definition, new_synonyms, new_examples)

        elif choice == '3':
            word_to_update = input("Enter a word to update its definition: ")
            new_definition = input("Enter the new definition: ")
            update_definition(dictionary, word_to_update, new_definition)

        elif choice == '4':
            display_all_words(dictionary)

        elif choice == '5':
            print("Saving data and exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()
