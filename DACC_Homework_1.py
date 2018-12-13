"""
dacc_homework_1.py
author: Hiteshi Shah
date: 9/8/2018
description: To implement Zipf's law
"""

import matplotlib.pyplot as plt
import math
import re
from nltk.corpus import stopwords

def zipfs_law(txt, remove_stop_words=None):
    '''
    function that shows the Zipf's Law plot for the given text file
    :param txt: name of the text file
    :param remove_stop_words: True if stop words need to be removed
    '''
    file_name = open(txt, 'r')
    file = file_name.read()
    file = re.sub(r'[^-\'\w]', ' ', file)
    words = file.split()
    words = [x.lower() for x in words]

    if remove_stop_words:
        stop_words = set(stopwords.words('english'))
        new_words = []
        for word in words:
            if word not in stop_words:
                new_words.append(word)

        words = new_words

    word_frequency = {}

    for word in words:
        words_list = list(word_frequency.keys())
        if word in words_list:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    no_of_words = len(sorted_word_frequency)
    if remove_stop_words:
        print("STOP WORDS REMOVAL")
    print("10 most frequent words in " + txt + ":", sorted_word_frequency[:10])
    print("3 least frequent words in " + txt + ":", sorted_word_frequency[no_of_words-4:no_of_words-1])
    print("-------------------------------------------------------------------------------------------")

    log10_frequencies = []
    log10_ranks = []
    rank = 1

    for item in sorted_word_frequency:
        log10_frequencies.append(math.log10(item[1]))
        log10_ranks.append(math.log10(rank))
        rank += 1

    plt.plot(log10_ranks, log10_frequencies)
    plt.xlabel("log10Rank")
    plt.ylabel("log10Frequency")
    if remove_stop_words:
        plt.title("Zipf's Law plot for " + txt + " with stop words removal")
    else:
        plt.title("Zipf's Law plot for " + txt)
    plt.show()

def main():
    file_names = ['17170-0', 'pg17606', 'Vegetius']
    for txt in file_names:
        zipfs_law(txt + '.txt')
        zipfs_law(txt + '.txt', True)

main()