# -*- coding: utf-8 -*-

# import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re
import json
import string
import nltk
from nltk.corpus import stopwords

uri_re = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'

def stripTagsAndUris(x):
    if x:
        # BeautifulSoup on content
        soup = BeautifulSoup(x, "html.parser")
        # Stripping all <code> tags with their content if any
        if soup.code:
            soup.code.decompose()
        # Get all the text out of the html
        text =  soup.get_text()
        # Returning text stripping out all uris
        return re.sub(uri_re, "", text)
    else:
        return ""
    
    
def removePunctuation(x):
    # Lowercasing all words
    x = x.lower()
    # Removing non ASCII chars
    x = re.sub(r'[^\x00-\x7f]',r' ',x)
    # Removing (replacing with empty spaces actually) all the punctuations
    return re.sub("["+string.punctuation+"]", " ", x)



stops = set(stopwords.words("english"))
def removeStopwords(x):
    # Removing all the stopwords
    filtered_words = [word for word in x.split() if word not in stops]
    return " ".join(filtered_words)


def cleaning_data():
    questionsDB = open('questions.txt')
    questions = []
    for questionLine in questionsDB.readlines():
        new_question ={}
        question = json.loads(questionLine)
        new_question['question']=question['title'] + " "+question['body']
        new_question["tags"]=question["tags"]
        questions.append(new_question)


    for data in questions:
        data["question"]=stripTagsAndUris(data["question"])
        data["question"]=removePunctuation(data["question"])
        data["question"]=removeStopwords(data["question"])


    file = open('questions_processed.txt', 'w')
    for question in questions:
        file.write(str(json.dumps(question))+'\n')
    file.close()