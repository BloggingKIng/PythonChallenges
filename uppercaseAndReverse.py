# code a function named uppercase_and_reverse that acceppts a sentence
# It should convert the sentence to uppercase form 
# And then should reverse the sentence
# It should return the uppercased and reversed sentence

def uppercase_and_reverse(sentence):
    uppercase = sentence.upper()
    uppercase_list = list(uppercase)
    uppercase_list.reverse()
    result = "".join(uppercase_list)
    return result


print(uppercase_and_reverse("Hi there, I would be uppercased and reversed"))