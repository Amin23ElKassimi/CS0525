def remove_punctuation(text):
    result = ""
    for char in text:
        if char.isalpha() or char.isspace():
            result += char
    return result.lower()

sample_text = "Hello, world! Python is fun; isn't it?"
cleaned_text = remove_punctuation(sample_text)
print(cleaned_text)