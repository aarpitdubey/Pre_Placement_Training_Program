# 37. Write a Python program to reverse the order of words in a sentence while preserving the word order

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)
print("Reversed sentence:", reversed_sentence)
