# 20. Implement a function to reverse the order of words in a given sentence.

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
result = reverse_sentence(input_sentence)
print("Reversed sentence:", result)
