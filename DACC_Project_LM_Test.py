"""
dacc_project_lm_test.py
author: Hiteshi Shah
date: 11/25/2018
description: To generate a test file for testing the language models
"""

import csv
import random

def clean_sentence(sentence):
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(",", "")
    sentence = sentence.replace("'", "")
    sentence = sentence.replace("-", " ")
    sentence = sentence.replace("[", "")
    sentence = sentence.replace("]", "")
    sentence = sentence.replace("(", "")
    sentence = sentence.replace(")", "")
    sentence = sentence.replace("%", "")
    sentence = sentence.replace(":", "")
    sentence = sentence.replace('"', "")
    sentence = sentence.replace("?", "")
    sentence = sentence.replace("!", "")

    return sentence

test_sentences = []
test_subreddits = []
subreddits = ['music', 'gaming', 'science', 'food', 'politics']
#['anime', 'comicbooks', 'harrypotter', 'music', 'starwars']
corpus = []

with open('threads.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    corpus = list(reader)

row_count = len(corpus)

while True:
    r = random.randint(0, row_count)
    line = corpus[r]
    if(line[4] in subreddits):
        sentence = clean_sentence(line[1])
        test_sentences.append(sentence)
        test_subreddits.append(line[4])
        if(len(test_sentences) == 7500):
            break

with open('test.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerows(zip(test_sentences, test_subreddits))