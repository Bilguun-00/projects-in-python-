from cs50 import get_string

def count_letter(letters):
    letter = 0
    for i in range(len(letters)):
        if letters[i].isalpha():
            letter = letter + 1
    return letter

def count_word(words):
    word = 1
    for i in range(len(words)):
        if words[i] == " ":
            word = word + 1
    return word

def count_sentence(sentences):
    sentence = 0
    for i in range(len(sentences)):
        if sentences[i] == '.' or sentences[i] == '?' or sentences[i] == '!':
            sentence = sentence + 1
    return sentence


text = get_string("enter the text: ")
letters = count_letter(text)
words = count_word(text)
sentences = count_sentence(text)

L = letters / words * 100
S = sentences / words * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print("Grade", index)

print(letters)
print(words)
print(sentences)
