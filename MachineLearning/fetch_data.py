import requests
import json


class DataFetcher:
    def fetch(self):
        site = 'astronomy'
        questionsFile = open('questions.txt', 'w')
        url = 'https://api.stackexchange.com/2.2/questions?pagesize=100&order=desc&sort=votes&site=' + site + '&filter=withbody&page='
        for i in range(1, 1000):
            response = requests.get(url + str(i))
            if response.ok:
                print('.', end='', flush=True)
                page = json.loads(response.content.decode('utf-8'))
                questions = page['items']
                if questions:
                    for question in questions:
                        print(json.dumps(question), file=questionsFile)
                else:
                    print('exited_')
                    break
            else:
                print('exited')
                break
        questionsFile.close()

    def extractTags(self):
        questionsDB = open('questions.txt')
        tagsDB = open('tags.txt', 'w')
        tagsList = []
        questions = questionsDB.readlines()
        for questionLine in questions:
            question = json.loads(questionLine)
            tags = question['tags']
            for tag in tags:
                if tag not in tagsList:
                    tagsList.append(tag)
        for tag in tagsList:
            print(tag, file=tagsDB)
        tagsDB.close()
        questionsDB.close()