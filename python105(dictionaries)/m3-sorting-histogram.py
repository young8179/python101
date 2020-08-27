user_input = input("please enter sentence: ")
word_dict = {} 
def letter_count(sentence):
    sentence_split = sentence.lower().split()
    for word in sentence_split:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    sortted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    
    print("The top three words are:")
    for i, j in sortted_dict[0:3]:
        print(f"{i}: {j}")

letter_count(user_input)


