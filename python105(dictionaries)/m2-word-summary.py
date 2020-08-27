user_input = input("please enter sentence: ")

def letter_count(sentence):
    word_dict = {}
    sentence_split = sentence.lower().split()
    for word in sentence_split:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    return word_dict

result = letter_count(user_input)
print(result)
