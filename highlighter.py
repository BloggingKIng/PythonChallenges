# he highlight_word function changes the given word in a sentence to its upper-case version
# for example, highlight_word("Have a nice day", "nice") returns "Have a NICE day"


def highlight_word(sentence, word):
    uppercase = word.upper()
    sentence = sentence.replace(word, uppercase)
    return sentence

print(highlight_word("Hi there, How are you", "you"))