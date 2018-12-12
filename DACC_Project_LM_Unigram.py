"""
dacc_project_lm_unigram.py
author: Hiteshi Shah
date: 11/25/2018
description: To implement a language model classifier for different subreddits
"""

import csv

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

    model = dict()
    total_count = 0

    for sentence in corpus:
        for word in sentence:
            try:
                model[word] += 1
            except KeyError:
                model[word] = 1
                total_count += 1

    for word in model:
        model[word] /= total_count

    return model

def get_probability(lm, subreddit, test):
    lambda1 = 0.95
    lambda_unk = 1 - lambda1
    v = 1000000
    prob = 1.0
    words = 0
    unknown_words = 0
    for i in range(0, len(test)):
        words += 1
        p = lambda_unk / v
        try:
            p += lambda1 * lm[test[i]]
        except KeyError:
            unknown_words += 1
        prob *= p

    print(subreddit + " coverage = " + str(round((words - unknown_words) / words * 100, 2)) + "%")

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
                test_sentence = [word for word in row[0].split()]
                best_prob = -1
                best_subreddit = ''
                for subreddit in subreddits:
                    prob = get_probability(lms[subreddit], subreddit, test_sentence)
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