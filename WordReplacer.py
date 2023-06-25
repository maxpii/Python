text = input("Give me some text: ")
word_to_replace = input("What do you want to replace? ")
word_to_sub = input("What do you want to put in place of word? (empty space to remove the word completely): ")
while word_to_replace in text:
    text = text[:text.index(word_to_replace)] + word_to_sub + text[text.index(word_to_replace)+len(word_to_replace):]
    print(text)
print("Here is your new text:\n" + text)