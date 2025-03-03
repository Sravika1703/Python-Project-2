import string

def count_words(text):
    for punctuation in string.punctuation:
        if punctuation != "'": 
            text = text.replace(punctuation, ' ')
    text = ' '.join(text.split())
    words = text.split()
    return len(words)
sentence = input("Enter a sentence or paragraph: ")
if not sentence.strip():
    print("Input is empty. Please enter some text.")
else:
    print(f"Word count: {count_words(sentence)}")
