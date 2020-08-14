import json

def adapt_data_to_naive_bayes():
    oldFile = open('questions_processed.txt')
    newFile = open('questions_processed_adapted.txt','w')

    for questionLine in oldFile.readlines():
        question = json.loads(questionLine)
        new_question=question['question'] + ";;" + question['tags'][0]
        newFile.write(new_question + '\n')
