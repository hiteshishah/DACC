"""
dacc_project_lm_trigram.py
author: Hiteshi Shah
date: 11/25/2018
description: To implement a language model classifier for different subreddits
"""

import csv
from nltk import trigrams
from collections import defaultdict

def language_model(file):
    corpus = []

    with open(file + '.csv', 'r', encoding='utf8') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        count = 0
        for row in data:
            if(row[1] != ''):
                corpus.append([word for word in row[1].split()])
                count += 1
            if count == 3500:
                break

    model = defaultdict(lambda: defaultdict(lambda: 0))

    for sentence in corpus:
        for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
            model[(w1, w2)][w3] += 1

    for w1_w2 in model:
        total_count = float(sum(model[w1_w2].values()))
        for w3 in model[w1_w2]:
            model[w1_w2][w3] /= total_count

    return model

def get_probability(lm, test):
    lambda1 = 0.95
    lambda2 = 0.95
    v = 1000000
    prob = 1.0
    for i in range(0, len(test) - 2):
        p1 = lambda1 * float(sum(lm[(test[i], test[i + 1])].values())) + (1 - lambda1) / v
        p2 = lambda2 * lm[(test[i], test[i + 1])][test[i + 2]] + (1 - lambda2) * p1
        prob *= p2

    return prob

def main():
    files = ['entertainment_music', 'gaming_gaming', 'learning_science', 'lifestyle_food', 'news_politics']
    #['entertainment_anime', 'entertainment_comicbooks', 'entertainment_harrypotter', 'entertainment_music', 'entertainment_starwars']
    subreddits = []
    lms = {}
    for file in files:
        subreddit = file.split("_")[1]
        subreddits.append(subreddit)
        lms[subreddit] = language_model(file)

    with open('test.csv', 'r', encoding='utf8', errors='ignore') as csvfile:
        data = csv.reader(csvfile)
        row_count = 0
        accuracy_count = 0
        for row in data:
            if(len(row) != 0):
                row_count += 1
                print(row[0])
                test_sentence = [None, None]
                for word in row[0].split():
                    test_sentence.append(word)
                best_prob = -1
                best_subreddit = ''
                for subreddit in subreddits:
                    prob = get_probability(lms[subreddit], test_sentence)
                    if prob > best_prob:
                        best_prob = prob
                        best_subreddit = subreddit
                if(best_subreddit == row[1]):
                    accuracy_count += 1
                print("classified as - /r/" + best_subreddit)
                print("originally from - /r/" + row[1])
                print()
        print("Accuracy: " + str(accuracy_count / row_count * 100) + "%")

main()