#!/usr/bin/env python3

# Define a class named MyString
class MyString:
    def __init__(self, value=None):
        # Initialize the class with a value attribute
        self.value = None
        
        # Check if a value was provided during initialization
        if value is not None:
            # Check if the provided value is a string
            if isinstance(value, str):
                self.value = value
            else:
                print("The value must be a string.")
        else:
            print("The value must be a string.")
            
    # Method to check if the string ends with a period, indicating a sentence
    def is_sentence(self):
        return self.value.endswith('.')
    
    # Method to check if the string ends with a question mark, indicating a question
    def is_question(self):
        return self.value.endswith('?')
    
    # Method to check if the string ends with an exclamation mark, indicating an exclamation
    def is_exclamation(self):
        return self.value.endswith('!')
    
    # Method to count the total number of sentences in the string
    def count_sentences(self):
        if self.value is None:
            return 0
        
        # Split the string using periods, question marks, and exclamation marks as separators
        sentences = [sentence.strip() for sentence in self.value.replace('?', '.').replace('!', '.').split('.') if sentence.strip()]
        return len(sentences)
      
      
# Create an instance of the MyString class with a sample string
my_string = MyString("Hello world! One! Two. Three?")

# Check if the string is considered a sentence
print(my_string.is_sentence())       # Output: False (ends with "?")

# Check if the string is considered a question
print(my_string.is_question())       # Output: True (ends with "?")

# Check if the string is considered an exclamation
print(my_string.is_exclamation())    # Output: False (ends with "?")

# Count the total number of sentences in the string
print(my_string.count_sentences())   # Output: 4
