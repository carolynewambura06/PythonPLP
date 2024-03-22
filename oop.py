import json
import difflib

# Function to load JSON data
def load_dictionary(file):
    with open(r'C:\Users\user\PythonPLP\data.json', 'r') as file:
        return json.load(file)
    
def get_definition(word, dictionary):
 word = word.lower()
 if word in dictionary:
  return dictionary[word]
 else:
  return None
 
def suggest_word(word,dictionary):
 suggestions = difflib.get_close_matches(word, dictionary.keys(),n=1)
 if suggestions:
  return suggestions[0]
 else:
  return None
 
 # Load the dictionary
dictionary = load_dictionary('data.json')

# User input loop
while True:
    user_word = input("Enter a word (or type 'exit' to quit): ")
    if user_word.lower() == 'exit':
        break

    definition = get_definition(user_word, dictionary)
    if definition:
        print(f"Definition: {definition}")
    else:
        suggestion = suggest_word(user_word, dictionary)
        if suggestion:
            print(f"Did you mean '{suggestion}'? Its definition is: {get_definition(suggestion, dictionary)}")
        else:
            print("Word not found in the dictionary.")


        

