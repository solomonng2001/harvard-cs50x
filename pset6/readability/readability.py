from cs50 import get_string


def main():
    # Get user input text
    text = get_string("Text: ")
    
    # Calculation of Coleman_Liau index and relevant variables
    l = count_letters(text) / count_words(text) * 100
    s = count_sentences(text) / count_words(text) * 100
    coleman_liau_index = 0.0588 * l - 0.296 * s - 15.8
    
    # Printing grade levels
    if coleman_liau_index < 1:
        print("Before Grade 1")
    elif coleman_liau_index >= 16:
        print("Grade 16+")
    else:
        print("Grade {}".format(round(coleman_liau_index)))


# Count words by assuming space between words
def count_words(text):
    successive_letter_count = 0
    word_count = 0
    for char in text:
        if char.isalpha():
            successive_letter_count += 1
        # Checking that word consists of at least 1 successive alphabet
        if char == " " and successive_letter_count > 0:
            word_count += 1
            successive_letter_count = 0
    return word_count + 1


# Count letters by counting only alphabet characters
def count_letters(text):
    letter_count = 0
    for char in text:
        if char.isalpha():
            letter_count += 1
    return letter_count


# Count sentences using end-of-sentence punctuation
def count_sentences(text):
    sentence_count = 0
    for char in text:
        if char == '.' or char == '?' or char == '!':
            sentence_count += 1
    return sentence_count


if __name__ == "__main__":
    main()