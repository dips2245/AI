import nltk
nltk.download("book")
sentence = "Tokenization is the process of breaking text into smaller units called tokens."
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
