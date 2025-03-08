# Required Filename: word_counter_functions.py

def get_sentence_input() -> str:
    """
    Prompts the user to enter a sentence and returns the input.
    
    :return: The user's sentence as a string.
    """
    return input("Enter a sentence: ")

def count_words(sentence: str) -> int:
    """
    Counts the number of words in the given sentence.
    
    :param sentence: A string representing the sentence.
    :return: The number of words in the sentence.
    """
    # Split the sentence into words based on spaces and return the length of the resulting list
    words = sentence.split()
    return len(words)

def main():
    """
    Main function to execute the word counting program.
    """
    # Get the sentence input from the user
    sentence = get_sentence_input()
    
    # Count the number of words in the sentence
    word_count = count_words(sentence)
    
    # Display the word count result
    print(f"The sentence has {word_count} words.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
