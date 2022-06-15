from data import words
import random

word = []
word_cpy = random.choice(words)

for _ in word_cpy:
    word.append(_)

word = tuple(word)
