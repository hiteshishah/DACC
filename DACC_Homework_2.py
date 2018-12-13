"""
dacc_homework_2.py
author: Hiteshi Shah (hss7374)
date: 9/23/2018
"""

import nltk
import statistics
import re
from nltk.parse import stanford
import os

java_path = "C:/Program Files/Java/jdk1.8.0_102/bin/java.exe"
os.environ['JAVAHOME'] = java_path
os.environ['STANFORD_PARSER'] ='C:\\Users\\hites\\Documents\\Data Analytics Cognitive Comp\\stanford-parser'
os.environ['STANFORD_MODELS'] ='C:\\Users\\hites\\Documents\\Data Analytics Cognitive Comp\\stanford-parser'

prefixes = "(1|www|_a_|A|E|H|L|M|T|W|PGDP|Fig|Figs)[.]"
verb_tags = ['VB', 'VBD', 'VBN', 'VBP', 'VBZ']

def pos_tagging(sentence):
    print("Tags:", nltk.pos_tag(nltk.word_tokenize(sentence)))

    sp = stanford.StanfordParser()
    trees = [tree for tree in sp.parse(sentence.split())]
    t = nltk.tree.Tree.fromstring(str(trees[0]))
    for rule in t.productions():
        st = rule.unicode_repr()
        expr = st.split("->")
        if expr[0] not in dt.keys():
            dt[expr[0]] = [expr[1]]
        else:
            if expr[1] not in dt[expr[0]]:
                dt[expr[0]].append(expr[1])
            else:
                repeating_patterns.append(expr[0] + " -> " + expr[1])

def sentence_length(txt):
    print(txt + ":")
    file_name = open(txt, encoding='utf-8')
    file = file_name.read()

    file = re.sub(prefixes, "555\n", file)
    pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
    sentences = pat.findall(file)
    sentence_lengths = {}
    for sentence in sentences:
        if re.search(r'[0-9]\n', sentence) == None:
            sentence = " ".join(sentence.split())
            if sentence.count(' ') >= 2:
                tags = nltk.pos_tag(nltk.word_tokenize(sentence))
                flag = False
                for tag in tags:
                    if tag[1] in verb_tags:
                        flag = True
                        break
                if flag:
                    sentence_lengths[sentence] = len(sentence)

    sentences = list(sentence_lengths.keys())
    lengths = list(sentence_lengths.values())
    max_length = max(lengths)
    min_length = min(lengths)
    max_length_sentence = sentences[lengths.index(max_length)]
    min_length_sentence = sentences[lengths.index(min_length)]
    mean_sentence_length = statistics.mean(lengths)
    stdev_sentence_length = statistics.stdev(lengths)

    print("Mean Sentence Length: " + str(mean_sentence_length))
    print("Stdev Sentence Length: " + str(stdev_sentence_length))
    print("Max Length: " + str(max_length))
    print("Longest Sentence: " + max_length_sentence)

    pos_tagging(max_length_sentence)

    print("Min Length: " + str(min_length))
    print("Shortest Sentence: " + min_length_sentence)

    pos_tagging(min_length_sentence)

def main():
    global dt
    dt = {}
    global repeating_patterns
    repeating_patterns = []
    file_names = ['17170-0', 'pg17606', 'Vegetius']
    for txt in file_names:
        sentence_length(txt + '.txt')
        print()

    print("Patterns that repeat in all three trees:")
    for pattern in repeating_patterns:
        print(pattern, end=', ')

    print()
    print("\nCFG for the parse trees of the three longest sentences:")
    for key in dt:
        v = " |".join(dt[key])
        print(key, ' -> ', v)

main()