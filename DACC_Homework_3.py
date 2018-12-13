"""
dacc_homework_3.py
author: Hiteshi Shah
date: 10/30/2018
description: To implement LDA and LSA
"""

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import time

inverted_index_docs = {}
inverted_index_topic_model = {}
topic_model_words = []
total_words = 0

def clean(sentence):
    stop_words = set(stopwords.words('english'))
    lemma = WordNetLemmatizer()
    remove_stop_words = " ".join([word for word in sentence.lower().split() if word not in stop_words])
    remove_period = ''.join(ch for ch in remove_stop_words if ch != ".")
    cleaned_data = " ".join(lemma.lemmatize(word) for word in remove_period.split() if re.search(r'([0-9]|\_)', word) == None and len(word) != 1)

    return cleaned_data

def get_sentences(txt):
    file_name = open(txt + '.txt', 'r')
    file = file_name.read()
    file = re.sub(r'[^-\.\w]', ' ', file)

    pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
    sentences = pat.findall(file)
    clean_sentences = [clean(sentence) for sentence in sentences]

    return clean_sentences

def lsa(txt):
    sentences = get_sentences(txt)

    vectorizer = TfidfVectorizer(stop_words='english',
                                 use_idf=True,
                                 smooth_idf=True)

    svd_model = TruncatedSVD(n_components=5,
                             algorithm='randomized',
                             n_iter=10)

    svd_transformer = Pipeline([('tfidf', vectorizer),
                                ('svd', svd_model)])

    svd_transformer.fit_transform(sentences)

    terms = vectorizer.get_feature_names()

    for i, comp in enumerate(svd_model.components_):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:5]
        print('Topic: %d' % i)
        print('  %s' % ', '.join(t[0] for t in sorted_terms))


def lda(txt):
    sentences = get_sentences(txt)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sentences)

    vocab = vectorizer.get_feature_names()

    n_top_words = 5
    k = 5

    model = LatentDirichletAllocation(n_topics=k, random_state=100)

    model.fit_transform(X)

    topic_words = {}

    for topic, comp in enumerate(model.components_):
        word_idx = np.argsort(comp)[::-1][:n_top_words]
        topic_words[topic] = [vocab[i] for i in word_idx]

    for topic, words in topic_words.items():
        for word in words:
            if word not in topic_model_words:
                topic_model_words.append(word)
        print('Topic: %d' % topic)
        print('  %s' % ', '.join(words))

def get_words(txt):
    sentences = get_sentences(txt)
    corpus = " ".join(sentence for sentence in sentences)
    words = [x.lower() for x in corpus.split()]

    return words

def set_inverted_index_docs(doc_no, txt):
    words = get_words(txt)
    global total_words
    total_words += len(words)

    for word in words:
        if word in inverted_index_docs:
            doc_list = inverted_index_docs[word]
            if doc_no not in doc_list:
                inverted_index_docs[word].append(doc_no)
        else:
            inverted_index_docs[word] = [doc_no]

def set_inverted_index_topic_model(doc_no, txt):
    words = get_words(txt)

    for word in topic_model_words:
        if word in words:
            if word in inverted_index_topic_model:
                doc_list = inverted_index_topic_model[word]
                if doc_no not in doc_list:
                    inverted_index_topic_model[word].append(doc_no)
            else:
                inverted_index_topic_model[word] = [doc_no]

def main():
    file_names = ['17170-0', 'pg17606', 'Vegetius']
    print("LSA:")
    start_time = time.time()
    for txt in file_names:
        print(txt + ".txt")
        lsa(txt)
        print()
    print("Execution time: " + str(time.time() - start_time) +" seconds")

    print("-----------------------------------------------------------------------------------------------------------")

    print("LDA:")
    start_time = time.time()
    for txt in file_names:
        print(txt + ".txt")
        lda(txt)
        print()
    print("Execution time: " + str(time.time() - start_time) + " seconds")

    print("-----------------------------------------------------------------------------------------------------------")

    print("Inverted Index using Docs:")
    start_time = time.time()
    doc_no = 0
    for txt in file_names:
        print("Document " + str(doc_no) + ": " + txt + ".txt", end = ", ")
        set_inverted_index_docs(doc_no, txt)
        doc_no += 1
    print()
    i = 0
    for key, value in inverted_index_docs.items():
        print(key + ": " + ', '.join(str(v) for v in value), end="; ")
        i += 1
        if i % 14 == 0:
            print()
    print()
    print()
    print("No. of words: " + str(total_words))
    print("Execution time: " + str(time.time() - start_time) + " seconds")

    print("-----------------------------------------------------------------------------------------------------------")

    print("Inverted Index using Topic Model:")
    start_time = time.time()
    doc_no = 0
    for txt in file_names:
        print("Document " + str(doc_no) + ": " + txt + ".txt", end=", ")
        set_inverted_index_topic_model(doc_no, txt)
        doc_no += 1
    print()
    i = 0
    for key, value in inverted_index_topic_model.items():
        print(key + ": " + ', '.join(str(v) for v in value), end="; ")
        i += 1
        if i % 12 == 0:
            print()
    print()
    print()
    print("No. of words: " + str(len(topic_model_words)))
    print("Execution time: " + str(time.time() - start_time) + " seconds")

main()